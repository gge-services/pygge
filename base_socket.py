import websocket
from threading import Event
import json
import re


class BaseSocket(websocket.WebSocketApp):
    def __init__(self, url, server_header, on_send=None, on_open=None, on_message=None, on_error=None, on_close=None, *args, **kwargs):
        super().__init__(url, on_open=self.onopen, on_message=self.onmessage, on_error=on_error, on_close=self.onclose, *args, **kwargs)
        self.server_header = server_header
        self.on_send = on_send
        self.on_open_param = on_open
        self.on_message_param = on_message
        self.on_close_param = on_close
        self.opened = Event()
        self.closed = Event()
        self.messages = []

    def onopen(self, ws):
        self.opened.set()
        self.on_open_param and self.on_open_param(ws)

    def onclose(self, ws, close_status_code, close_msg):
        self.opened.clear()
        self.closed.set()
        self.on_close_param and self.on_close_param(ws, close_status_code, close_msg)

    def send(self, data, *args, **kwargs):
        self.on_send and self.on_send(data)
        return super().send(data, *args, **kwargs)

    def send_json_command(self, command, data):
        self.send_command_message(['xt', self.server_header, command, '1', json.dumps(data)])
    
    def send_raw_command(self, command, data):
        self.send_command_message(['xt', self.server_header, command, '1', *data])
    
    def send_empty_command(self, command):
        self.send_command_message(['xt', self.server_header, command, '1'])
    
    def send_command_message(self, data):
        self.send('%'.join(['', *data, '']))
    
    def send_xml_message(self, t, action, r, data):
        self.send(f"<msg t='{t}'><body action='{action}' r='{r}'>{data}</body></msg>")

    def wait_for_json_response(self, command, data=False, timeout=5):
        return self.wait_for_response("json", {
            "command": command,
            "data": data
        }, timeout=timeout)
    
    def wait_for_xml_response(self, t, action, r, timeout=5):
        self.wait_for_response("xml", {
            "t": t,
            "action": action,
            "r": r,
        }, timeout=timeout)

    def wait_for_response(self, type, conditions, timeout=5):
        event = Event()
        message = {
            "type": type,
            "conditions": conditions,
            "event": event
        }
        self.messages.append(message)
        result = event.wait(timeout)
        if not result:
            raise TimeoutError("Timeout waiting for response")
        response = message["response"]
        self.messages.remove(message)
        return response
    
    def raise_for_status(self, response, expected_status=0):
        if response["type"] == "json" and response["payload"]["status"] != expected_status:
            raise Exception(f"Unexpected status: {response['payload']['status']}")

    def parse_response(self, response):
        if response.startswith("<"):
            response = re.search(r"<msg t='(.*?)'><body action='(.*?)' r='(.*?)'>(.*?)</body></msg>", response).groups()
            return {
                "type": "xml",
                "payload": {
                    "t": response[0],
                    "action": response[1],
                    "r": response[2],
                    "data": response[3]
                }
            }
        else:
            response = response.strip("%").split("%")
            response = {
                "type": "json",
                "payload": {
                    "command": response[1],
                    "status": int(response[3]),
                    "data": "%".join(response[4:]) if len(response) > 4 else None
                }
            }
            if response["payload"]["data"] and response["payload"]["data"].startswith("{"):
                response["payload"]["data"] = json.loads(response["payload"]["data"])
            return response
    
    def process_response(self, response):
        for message in self.messages:
            if ((
                "json" == response["type"] == message["type"] and
                message["conditions"]["command"] == response["payload"]["command"] and (
                    message["conditions"]["data"] == False or
                    (message["conditions"]["data"] == True and response["payload"]["data"] != None) or
                    None == message["conditions"]["data"] == response["payload"]["data"] or
                    {} == message["conditions"]["data"] == response["payload"]["data"] or (
                        isinstance(response["payload"]["data"], dict) and
                        isinstance(message["conditions"]["data"], dict) and
                        all(key in response["payload"]["data"] and response["payload"]["data"][key] == value for key, value in message["conditions"]["data"].items())
                    )
                )
            ) or
            (
                "xml" == response["type"] == message["type"] and
                message["conditions"]["t"] == response["payload"]["t"] and
                message["conditions"]["action"] == response["payload"]["action"] and
                message["conditions"]["r"] == response["payload"]["r"]
            )):
                message["response"] = response
                message["event"].set()
                break

    def onmessage(self, ws, message):
        message = message.decode('UTF-8')
        response = self.parse_response(message)
        self.process_response(response)
        self.on_message_param and self.on_message_param(ws, message)
