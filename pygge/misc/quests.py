from ..base_gge_socket import BaseGgeSocket

class Quests(BaseGgeSocket):
    def get_quests(self, sync=True, quiet=False):
        try:
            self.send_json_command("dcl", {
                "CD": 1
            })
            if sync:
                response = self.wait_for_json_response("dcl")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def complete_message_quest(self, quest_id, sync=True, quiet=False):
        try:
            self.send_json_command("qsc", {
                "QID": quest_id
            })
            if sync:
                response = self.wait_for_json_response("qsc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def complete_donation_quest(self, quest_id, food=0, wood=0, stone=0, gold=0, oil=0, coal=0, iron=0, glass=0, sync=True, quiet=False):
        try:
            self.send_json_command("qdr", {
                "QID": quest_id,
                "F": food,
                "W": wood,
                "S": stone,
                "C1": gold,
                "O": oil,
                "C": coal,
                "I": iron,
                "G": glass,
                "PWR": 0,
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("qdr")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def tracking_recommended_quests(self, quiet=False):
        try:
            self.send_json_command("ctr", {
                "TRQ": 0
            })
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        

    def complete_quest_condition(self, quest_id, condition, sync=True, quiet=False):
        try:
            self.send_json_command("fcq", {
                "QTID": quest_id,
                "QC": condition
            })
            if sync:
                response = self.wait_for_json_response("fcq")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def wait_finish_quest(self, quest_id, timeout=5, quiet=False):
        try:
            response = self.wait_for_json_response("qfi", {
                "QID": quest_id
            }, timeout=timeout)
            self.raise_for_status(response)
            return response
        except Exception as e:
            if not quiet:
                raise e
            return False
