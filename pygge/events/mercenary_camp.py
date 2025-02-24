from ..base_gge_socket import BaseGgeSocket

class MercenaryCamp(BaseGgeSocket):
    def get_mercenary_missions(self, sync=True, quiet=False):
        try:
            self.send_json_command("mpe", {
                "MID": -1
            })
            if sync:
                response = self.wait_for_json_response("mpe")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def refresh_mercenary_mission(self, mission_id, sync=True, quiet=False):
        try:
            self.send_json_command("rmm", {
                "MID": mission_id
            })
            if sync:
                response = self.wait_for_json_response("rmm")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def start_mercenary_mission(self, mission_id, sync=True, quiet=False):
        try:
            self.send_json_command("mpe", {
                "MID": mission_id
            })
            if sync:
                response = self.wait_for_json_response("mpe")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def skip_mercenary_mission(self, mission_id, sync=True, quiet=False):
        try:
            self.send_json_command("mpe", {
                "MID": mission_id
            })
            if sync:
                response = self.wait_for_json_response("mpe")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def collect_mercenary_mission(self, mission_id, sync=True, quiet=False):
        try:
            self.send_json_command("mpe", {
                "MID": mission_id
            })
            if sync:
                response = self.wait_for_json_response("mpe")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
