from ..base_socket import BaseSocket

class DailyGifts(BaseSocket):
    def collect_daily_gift(self, choice, sync=True, quiet=False):
        # choice: "MS1", "F", "U" + wod_id
        try:
            self.send_json_command("clb", {
                "ID": -1,
                "I": choice,
                "SP": None
            })
            if sync:
                response = self.wait_for_json_response("clb")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def collect_daily_gift_vip(self, sync=True, quiet=False):
        try:
            self.send_json_command("clb", {
                "ID": -1,
                "I": None,
                "SP": "VIP"
            })
            if sync:
                response = self.wait_for_json_response("clb")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def collect_daily_gift_alliance(self, sync=True, quiet=False):
        try:
            self.send_json_command("clb", {
                "ID": -1,
                "I": None,
                "SP": "ALLI"
            })
            if sync:
                response = self.wait_for_json_response("clb")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
