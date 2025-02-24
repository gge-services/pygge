from ..base_gge_socket import BaseGgeSocket

class Lords(BaseGgeSocket):
    def get_lords(self, sync=True, quiet=False):
        try:
            self.send_json_command("gli", {})
            if sync:
                response = self.wait_for_json_response("gli")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False