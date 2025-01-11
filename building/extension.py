from ..base_socket import BaseSocket

class Extension(BaseSocket):
    def buy_extension(self, x, y, rotated, sync=True, quiet=False):
        try:
            self.send_json_command("ebe", {
                "X": x,
                "Y": y,
                "R": rotated,
                "CT": 1
            })
            if sync:
                response = self.wait_for_json_response("ebe")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def collect_extension_gift(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("etc", {
                "OID": building_id
            })
            if sync:
                response = self.wait_for_json_response("etc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
