"""
This module contains the base class for Goodgame Empire websocket connections.

The `BaseGgeSocket` class is a subclass of `websocket.WebSocketApp` and provides additional functionality for sending and receiving messages.
"""

import json
import re
import threading
from typing import Callable

import websocket


class BaseGgeSocket(websocket.WebSocketApp):
    """
    Base class for Goodgame Empire websocket connections.

    This class is a subclass of websocket.WebSocketApp and provides additional functionality for sending and receiving messages.

    Attributes:
        server_header (str): The server header to use.
        opened (threading.Event): An event that is set when the connection is opened.
        closed (threading.Event): An event that is set when the connection is closed.
    """

    def __init__(
        self,
        url: str,
        server_header: str,
        on_send: Callable[[websocket.WebSocketApp, str], None] | None = None,
        on_open: Callable[[websocket.WebSocketApp], None] | None = None,
        on_message: Callable[[websocket.WebSocketApp, str], None] | None = None,
        on_error: Callable[[websocket.WebSocketApp, Exception], None] | None = None,
        on_close: Callable[[websocket.WebSocketApp, int, str], None] | None = None,
        *args,
        **kwargs,
    ) -> None:
        """
        Initializes the websocket connection.

        Args:
            url (str): The URL of the websocket server.
            server_header (str): The server header to use.
            on_send (function, optional): A function to call when sending a message. Defaults to None.
            on_open (function, optional): A function to call when the connection is opened. Defaults to None.
            on_message (function, optional): A function to call when a message is received. Defaults to None.
            on_error (function, optional): A function to call when an error occurs. Defaults to None.
            on_close (function, optional): A function to call when the connection is closed. Defaults to None.
            *args: Additional arguments to pass to the websocket.WebSocketApp constructor.
            **kwargs: Additional keyword arguments to pass to the websocket.WebSocketApp constructor.

        Returns:
            None
        """
        # print(f"BaseGgeSocket initialized with url: {url}")
        # print(f"BaseGgeSocket initialized with server_header: {server_header}")
        super().__init__(
            url,
            on_open=self.__onopen,
            on_message=self.__onmessage,
            on_error=self.__onerror,
            on_close=self.__onclose,
            *args,
            **kwargs,
        )
        self.send_lock = threading.Lock()
        self.server_header = server_header
        """ str: The server header to use. """
        self.__on_send = on_send
        """ function | None: A function to call when sending a message. """
        self.__on_open = on_open
        """ function | None: A function to call when the connection is opened. """
        self.__on_error = on_error
        """ function | None: A function to call when an error occurs. """
        self.__on_message = on_message
        """ function | None: A function to call when a message is received. """
        self.__on_close = on_close
        """ function | None: A function to call when the connection is closed. """
        self.opened = threading.Event()
        """ threading.Event: An event that is set when the connection is opened. """
        self.closed = threading.Event()
        """ threading.Event: An event that is set when the connection is closed. """
        self.__messages: list[dict] = []
        """ list[dict]: Internal list of messages waiting for a response. """
        
        self.exempt_commands = {"rlu"}
        """ set[str]: Commands that are exempt from error handling and termination. """
        
        self.error_thresholds = {
            1: 2,     # general error
            2: 1,     # invalid parameter value
            3: 1,     # missing parameter
            4: 1,     # invalid wod id
            # 5: 36,     # invalid object id
            6: 1,     # invalid position
            10: 1,    # not enough coins
            11: 1,    # not enough rubies
            55: 1,    # not enough resources
            63: 1,    # no free construction slot
            88: 3,    # too many units - increased threshold
            90: 2,    # cant start new armies
            91: 1,    # invalid army request 
            95: 3,    # cooling down
            105: 1,   # not enough spies
            101: 1,   # missing units
            203: 5,   # invalid area
            256: 4,   # commander is used
            308: 1,   # not enough silver runes
            309: 1,   # not enough gold runes
            311: 50,  # not cooling down
            313: 1,   # attack too many units
            327: 2,   # not enough special currency
        }
        self.error_counts = {error_code: 0 for error_code in self.error_thresholds}
        self.ignore_error_thresholds = False
        self.error_lock = threading.Lock()

    def __onopen(self, ws: websocket.WebSocketApp) -> None:
        """
        Internal function which is called when the connection is opened.

        Args:
            ws (websocket.WebSocketApp): The websocket connection.

        Returns:
            None
        """
        self.opened.set()
        self.__on_open and self.__on_open(ws)

    def __onmessage(self, ws: websocket.WebSocketApp, message: bytes) -> None:
        """
        Internal function which is called when a message is received.

        Args:
            ws (websocket.WebSocketApp): The websocket connection.
            message (str): The message received.

        Returns:
            None
        """
        message = message.decode("UTF-8")
        response = self.parse_response(message)
        self.__process_response(response)
        self.__on_message and self.__on_message(ws, message)

    def __onerror(self, ws: websocket.WebSocketApp, error: Exception) -> None:
        """
        Internal function which is called when an error occurs.

        Args:
            ws (websocket.WebSocketApp): The websocket connection.
            error (Exception): The error that occurred.

        Returns:
            None
        """
        self.__on_error and self.__on_error(ws, error)

    def __onclose(
        self, ws: websocket.WebSocketApp, close_status_code: int, close_msg: str
    ) -> None:
        """
        Internal function which is called when the connection is closed.

        Args:
            ws (websocket.WebSocketApp): The websocket connection.
            close_status_code (int): The status code of the close.
            close_msg (str): The message of the close.

        Returns:
            None
        """
        self.opened.clear()
        self.closed.set()
        self.__on_close and self.__on_close(ws, close_status_code, close_msg)

    def send(self, data: str, *args, **kwargs) -> None:
        """
        Sends a message over the websocket connection.

        Args:
            data (str): The message to send.
            *args: Additional arguments to pass to the websocket.WebSocketApp.send method.
            **kwargs: Additional keyword arguments to pass to the websocket.WebSocketApp.send method.

        Returns:
            None
        """
        with self.send_lock:
            self.__on_send and self.__on_send(self, data)
            super().send(data, *args, **kwargs)

    def __send_command_message(self, data: list[str]) -> None:
        """
        Internal function which sends a command message over the websocket connection.

        Args:
            data (list[str]): The data to send.

        Returns:
            None
        """
        self.send("%".join(["", *data, ""]))

    def send_raw_command(self, command: str, data: list[str]) -> None:
        """
        Sends a raw command over the websocket connection.

        Args:
            command (str): The command to send.
            data (list[str]): The data to send.

        Returns:
            None
        """
        self.__send_command_message(["xt", self.server_header, command, "1", *data])

    def send_json_command(self, command: str, data: dict) -> None:
        """
        Sends a JSON command over the websocket connection.

        Args:
            command (str): The command to send.
            data (dict): The data to send.

        Returns:
            None
        """
        # self.__send_command_message(
        #     ["xt", self.server_header, command, "1", json.dumps(data)]
        # )
        self.__send_command_message(
            ["xt", self.server_header, command, "1", json.dumps(data, separators=(',', ':'))]
        )

    def send_xml_message(self, t: str, action: str, r: str, data: str) -> None:
        """
        Sends an XML message over the websocket connection.

        Args:
            t (str): The t attribute of the message.
            action (str): The action attribute of the message.
            r (str): The r attribute of the message.
            data (str): The data of the message.

        Returns:
            None
        """
        self.send(f"<msg t='{t}'><body action='{action}' r='{r}'>{data}</body></msg>")

    def __wait_for_response(
        self, type: str, conditions: dict, timeout: int = 5
    ) -> dict:
        """
        Internal function which waits for a response with the specified type and conditions.

        Args:
            type (str): The expected type of the response.
            conditions (dict): The expected conditions of the response.
            timeout (int, optional): The timeout to wait for the response. Defaults to 5.

        Returns:
            dict: The response.

        Raises:
            TimeoutError: If the response is not received within the timeout.
        """
        event = threading.Event()
        message = {
            "type": type,
            "conditions": conditions,
            "response": None,
            "event": event,
        }
        self.__messages.append(message)
        result = event.wait(timeout)
        self.__messages.remove(message)
        if not result:
            raise TimeoutError("Timeout waiting for response")
        response = message["response"]
        return response

    def wait_for_json_response(
        self, command: str, data: dict | bool = False, timeout: int = 5
    ) -> dict:
        """
        Waits for a JSON response with the specified command and data.

        Args:
            command (str): The expected command of the response.
            data (dict, optional): The expected data of the response. Defaults to False.
            timeout (int, optional): The timeout to wait for the response. Defaults to 5.

        Returns:
            dict: The response.

        Raises:
            TimeoutError: If the response is not received within the timeout.
        """
        return self.__wait_for_response(
            "json", {"command": command, "data": data}, timeout=timeout
        )

    def wait_for_xml_response(
        self, t: str, action: str, r: str, timeout: int = 5
    ) -> dict:
        """
        Waits for an XML response with the specified t, action, and r attributes.

        Args:
            t (str): The expected t attribute of the response.
            action (str): The expected action attribute of the response.
            r (str): The expected r attribute of the response.
            timeout (int, optional): The timeout to wait for the response. Defaults to 5.

        Returns:
            dict: The response.

        Raises:
            TimeoutError: If the response is not received within the timeout.
        """
        self.__wait_for_response(
            "xml",
            {
                "t": t,
                "action": action,
                "r": r,
            },
            timeout=timeout,
        )

    def raise_for_status(self, response: dict, expected_status: int = 0) -> None:
        """
        Raises an exception if the status of the response is not the expected status.

        Args:
            response (dict): The response to check.
            expected_status (int, optional): The expected status. Defaults to 0.

        Returns:
            None

        Raises:
            Exception: If the status of the response is not the expected status.
        """
        if (
            response["type"] == "json"
            and response["payload"]["status"] != expected_status
        ):
            raise Exception(f"Unexpected status: {response['payload']['status']}")

    def dispatch_raw_message(self, message):
        """
        Public method to dispatch messages through the same pipeline as __onmessage.
        This ensures that temp server messages are properly processed and wait conditions are fulfilled.
        
        Args:
            message (bytes|str): The raw message to dispatch
        """
        m = message.decode("UTF-8") if isinstance(message, (bytes, bytearray)) else str(message)
        response = self.parse_response(m)
        self.__process_response(response)
        if self.__on_message:
            self.__on_message(self, m)

    def parse_response(self, response: str) -> dict:
        """
        Parses a response into a dictionary with the type and payload.

        Args:
            response (str): The response to parse.

        Returns:
            dict: The parsed response.
        """
        if response.startswith("<"):
            response = re.search(
                r"<msg t='(.*?)'><body action='(.*?)' r='(.*?)'>(.*?)</body></msg>",
                response,
            ).groups()
            return {
                "type": "xml",
                "payload": {
                    "t": response[0],
                    "action": response[1],
                    "r": response[2],
                    "data": response[3],
                },
            }
        else:
            response = response.strip("%").split("%")
            parsed_response = {
                "type": "json",
                "payload": {
                    "command": response[1],
                    "status": int(response[3]),
                    "data": "%".join(response[4:]) if len(response) > 4 else None,
                },
            }
            if parsed_response["payload"]["data"] and parsed_response["payload"]["data"].startswith(
                "{"
            ):
                parsed_response["payload"]["data"] = json.loads(parsed_response["payload"]["data"])
            
            # Note: Error handling is done in __process_response to avoid duplicate processing
            return parsed_response

    def __process_response(self, response: dict) -> None:
        """
        Internal function which sets a waiting message as done if the response matches its conditions.

        Args:
            response (dict): The response to process.

        Returns:
            None
        """
        # Handle error status codes only for JSON responses and only once per WebSocket message
        if response["type"] == "json":
            status = response["payload"]["status"]
            if status != 0 and status <= 500:
                self.log_error_message(status, response["payload"]["command"], response["payload"].get("data"))

                if not self.ignore_error_thresholds and response["payload"]["command"] and response["payload"]["command"] not in self.exempt_commands:
                    self._handle_error_status(status, response["payload"]["command"])
        
        # Process waiting messages
        for message in self.__messages:
            if self.__compare_response(response, message):
                message["response"] = response
                message["event"].set()
                break

    def __compare_response(self, response: dict, expected: dict) -> bool:
        """
        Compares a response to an expected response.

        Args:
            response (dict): The response to compare.
            expected (dict): The expected response.

        Returns:
            bool: True if the response matches the expected response, False otherwise.
        """
        if "json" == response["type"] == expected["type"] and response["payload"]["command"] == expected["conditions"]["command"]:
            if expected["conditions"]["data"] == False:
                return True
            elif expected["conditions"]["data"] == True and response["payload"]["data"] != None:
                return True
            elif None == expected["conditions"]["data"] == response["payload"]["data"]:
                return True
            elif {} == expected["conditions"]["data"] == response["payload"]["data"]:
                return True
            elif isinstance(response["payload"]["data"], dict) and isinstance(expected["conditions"]["data"], dict):
                if self.__compare_nested_headers(expected["conditions"]["data"], response["payload"]["data"]):
                    return True
        elif "xml" == response["type"] == expected["type"]:
            if response["payload"]["t"] == expected["conditions"]["t"] and response["payload"]["action"] == expected["conditions"]["action"] and response["payload"]["r"] == expected["conditions"]["r"]:
                return True
        return False
    
    def __compare_nested_headers(self, message, response):
        if message is None or response is None:
            return False
        for key in message:
            if type(message) is not type(response):
                return False
            elif type(message[key]) is dict:
                if not self.__compare_nested_headers(message[key], response[key]):
                    return False
            else:
                if key not in response or response[key] != message[key]:
                    return False
        return True

    def log_error_message(self, status_code: int, command: str = None, data: dict = None):
        """
        Logs the incoming error message with status code.
        
        Args:
            status_code (int): The error status code
            command (str, optional): The command that caused the error
            data (dict, optional): Additional data from the response
        """
        if command and command in self.exempt_commands:
            return

        log_message = f"[ERROR {status_code}] Incoming message:"
        
        if command:
            log_message += f" Command: {command}"
        
        if data:
            log_message += f" | Data: {data}"
        
        # print(log_message)

    def _handle_error_status(self, status_code: int, command: str = None):
        """
        Handles error status codes with weighted counting and threshold-based termination.
        
        Args:
            status_code (int): The error status code
            command (str, optional): The command that caused the error
        """
        # Ignore error codes greater than 500
        if status_code > 500:
            return
            
        if status_code in self.error_thresholds:
            with self.error_lock:
                self.error_counts[status_code] += 1
                current_count = self.error_counts[status_code]
                threshold = self.error_thresholds[status_code]
                
                error_message = f"Error {status_code} occurred ({current_count}/{threshold})"
                if command:
                    error_message += f" in command '{command}'"
                
                print(f"[ERROR HANDLER] {error_message}")
                
                if current_count >= threshold:
                    self._terminate_bot_process(status_code, current_count)

    def _terminate_bot_process(self, status_code: int, count: int):
        """
        Terminates the bot process when error threshold is reached.
        
        Args:
            status_code (int): The error code that caused termination
            count (int): The number of times this error occurred
        """
        import sys
        import os
        
        termination_message = f"CRITICAL: Bot terminated due to error {status_code} occurring {count} times (threshold reached)"
        print(f"[BOT TERMINATION] {termination_message}")
        
        # Try to gracefully close the connection
        try:
            self.close()
        except:
            pass
        
        # Terminate the process
        os._exit(1)

    def get_error_statistics(self):
        """
        Returns current error statistics.
        
        Returns:
            dict: Dictionary with error codes as keys and their counts as values
        """
        with self.error_lock:
            return self.error_counts.copy()

