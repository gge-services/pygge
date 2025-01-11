from ..base_socket import BaseSocket

class Wall(BaseSocket):
    def upgrade_wall(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("eud", {
                "OID": building_id,
                "PWR": 0,
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("eud")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
