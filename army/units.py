from ..base_socket import BaseSocket

class Units(BaseSocket):
    def get_units_inventory(self, sync=True, quiet=False):
        try:
            self.send_json_command("gui", {})
            if sync:
                response = self.wait_for_json_response("gui")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def delete_units(self, wod_id, amount, sync=True, quiet=False):
        try:
            self.send_json_command("dup", {
                "WID": wod_id,
                "A": amount,
                "S": 0
            })
            if sync:
                response = self.wait_for_json_response("dup")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def wait_receive_units(self, kingdom, castle_id, wod_id, amount, timeout=5, quiet=False):
        try:
            response = self.wait_for_json_response("rue", {
                "AID": castle_id,
                "SID": kingdom,
                "WID": wod_id,
                "RUA": amount
            }, timeout=timeout)
            self.raise_for_status(response)
            return response
        except Exception as e:
            if not quiet:
                raise e
            return False
