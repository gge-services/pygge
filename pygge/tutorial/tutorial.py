from ..base_gge_socket import BaseGgeSocket

class Tutorial(BaseGgeSocket):
    def choose_hero(self, hero_id=802, sync=True, quiet=False):
        try:
            self.send_json_command("hdc", {
                "HID": hero_id
            })
            if sync:
                response = self.wait_for_json_response("hdc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def collect_noob_gift(self, sync=True, quiet=False):
        try:
            self.send_json_command("uoa", {})
            if sync:
                response = self.wait_for_json_response("uoa")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def skip_generals_intro(self, sync=True, quiet=False):
        try:
            self.send_json_command("sgi", {})
            if sync:
                response = self.wait_for_json_response("sgi")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
