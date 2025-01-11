from ..base_socket import BaseSocket

class Events(BaseSocket):
    def get_event_points(self, event_id, sync=True, quiet=False):
        try:
            self.send_json_command("pep", {
                "EID": event_id
            })
            if sync:
                response = self.wait_for_json_response("pep")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def get_ranking(self, ranking_type, category=-1, search_value=-1, sync=True, quiet=False):
        try:
            self.send_json_command("hgh", {
                "LT": ranking_type,
                "LID": category,
                "SV": search_value
            })
            if sync:
                response = self.wait_for_json_response("hgh")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def choose_event_difficulty(self, event_id, difficulty_id, premium_unlock=0, sync=True, quiet=False):
        try:
            self.send_json_command("sede", {
                "EID": event_id,
                "EDID": difficulty_id,
                "C2U": premium_unlock
            })
            if sync:
                response = self.wait_for_json_response("sede")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
