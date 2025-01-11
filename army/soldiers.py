from ..base_socket import BaseSocket

class Soldiers(BaseSocket):
    def get_recruitment_queue(self, sync=True, quiet=False):
        try:
            self.send_json_command("spl", {
                "LID": 0
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
    
    def recruit_soldiers(self, castle_id, wod_id, amount, sync=True, quiet=False):
        try:
            self.send_json_command("bup", {
                "LID": 0,
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
    
    def double_recruitment_slot(self, castle_id, slot, slot_type, sync=True, quiet=False):
        # slot_type: "production" or "queue"
        try:
            self.send_json_command("bou", {
                "LID": 0,
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


    def cancel_recruitment(self, slot, slot_type, sync=True, quiet=False):
        # slot_type: "production" or "queue"
        try:
            self.send_json_command("mcu", {
                "LID": 0,
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
    
    def ask_alliance_help_recruit(self, sync=True, quiet=False):
        try:
            self.send_json_command("ahr", {
                "ID": 0,
                "T": 6
            })
            if sync:
                response = self.wait_for_json_response("ahr")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
