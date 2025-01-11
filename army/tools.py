from ..base_socket import BaseSocket

class Tools(BaseSocket):
    def get_production_queue(self, sync=True, quiet=False):
        try:
            self.send_json_command("spl", {
                "LID": 1
            })
            if sync:
                response = self.wait_for_json_response("spl")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def produce_tools(self, castle_id, wod_id, amount, sync=True, quiet=False):
        try:
            self.send_json_command("bup", {
                "LID": 1,
                "WID": wod_id,
                "AMT": amount,
                "PO": -1,
                "PWR": 0,
                "SK": 73,
                "SID": 0,
                "AID": castle_id
            })
            if sync:
                response = self.wait_for_json_response("bup")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def double_production_slot(self, castle_id, slot, slot_type, sync=True, quiet=False):
        # slot_type: "production" or "queue"
        try:
            self.send_json_command("bou", {
                "LID": 1,
                "S": slot,
                "AID": castle_id,
                "SID": 0,
                "ST": slot_type
            })
            if sync:
                response = self.wait_for_json_response("bou")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def cancel_production(self, slot, slot_type, sync=True, quiet=False):
        try:
            self.send_json_command("mcu", {
                "LID": 1,
                "S": slot,
                "ST": slot_type
            })
            if sync:
                response = self.wait_for_json_response("mcu")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
