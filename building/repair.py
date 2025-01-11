from ..base_socket import BaseSocket

class Repair(BaseSocket):
    def repair_building(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("rbu", {
                "OID": building_id,
                "PO": -1,
                "PWR": 0
            })
            if sync:
                response = self.wait_for_json_response("rbu")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def ask_alliance_help_repair(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("ahr", {
                "ID": building_id,
                "T": 3
            })
            if sync:
                response = self.wait_for_json_response("ahr")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def repair_all(self, sync=True, quiet=False):
        try:
            self.send_json_command("ira", {})
            if sync:
                response = self.wait_for_json_response("ira")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
