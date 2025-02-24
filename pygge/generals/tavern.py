from ..base_gge_socket import BaseGgeSocket

class Tavern(BaseGgeSocket):
    def get_offerings_status(self, sync=True, quiet=False):
        try:
            self.send_json_command("gcs", {})
            if sync:
                response = self.wait_for_json_response("gcs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False