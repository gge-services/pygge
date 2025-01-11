from ..base_socket import BaseSocket

class Technicus(BaseSocket):

    def upgrade_equipment_technicus(self, equipment_id, premium=0, sync=True, quiet=False):
        try:
            self.send_json_command("eqe", {
                "C2": premium,
                "EID": equipment_id
            })
            if sync:
                response = self.wait_for_json_response("eqe")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
