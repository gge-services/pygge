from ..base_gge_socket import BaseGgeSocket

class Bookmarks(BaseGgeSocket):
    def get_bookmarks(self, sync=True, quiet=False):
        try:
            self.send_json_command("gbl", {})
            if sync:
                response = self.wait_for_json_response("gbl")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        