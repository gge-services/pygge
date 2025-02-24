from ..base_gge_socket import BaseGgeSocket

class WishingWell(BaseGgeSocket):
    def upgrade_wishing_well(self, sync=True, quiet=False):
        try:
            self.send_json_command("rww", {
                "PWR": 0,
                "_PO": -1,
                "WOP": "U"
            })
            if sync:
                response = self.wait_for_json_response("rww")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
