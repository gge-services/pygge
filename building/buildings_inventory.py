from ..base_socket import BaseSocket

class BuildingsInventory(BaseSocket):
    def store_building(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("sob", {
                "OID": building_id
            })
            if sync:
                response = self.wait_for_json_response("sob")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def sell_building_inventory(self, wod_id, amount, unique_id=-1, sync=True, quiet=False):
        try:
            self.send_json_command("sds", {
                "WID": wod_id,
                "AMT": amount,
                "UID": unique_id
            })
            if sync:
                response = self.wait_for_json_response("sds")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def get_building_inventory(self, sync=True, quiet=False):
        try:
            self.send_json_command("sin", {})
            if sync:
                response = self.wait_for_json_response("sin")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
