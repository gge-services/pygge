from ..base_socket import BaseSocket

class Help(BaseSocket):
    def help_alliance_member(self, kingdom, help_id, sync=True, quiet=False):
        try:
            self.send_json_command("ahc", {
                "LID": help_id,
                "KID": kingdom
            })
            if sync:
                response = self.wait_for_json_response("ahc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def help_alliance_all(self, kingdom, sync=True, quiet=False):
        try:
            self.send_json_command("aha", {
                "KID": kingdom
            })
            if sync:
                response = self.wait_for_json_response("aha")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
