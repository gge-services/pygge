from ..base_socket import BaseSocket

class Hospital(BaseSocket):
    def heal(self, wod_id, amount, sync=True, quiet=False):
        try:
            self.send_json_command("hru", {
                "U": wod_id,
                "A": amount
            })
            if sync:
                response = self.wait_for_json_response("hru")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def cancel_heal(self, slot_id, sync=True, quiet=False):
        try:
            self.send_json_command("hcs", {
                "S": slot_id
            })
            if sync:
                response = self.wait_for_json_response("hcs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def instant_heal(self, slot_id, sync=True, quiet=False):
        try:
            self.send_json_command("hss", {
                "S": slot_id
            })
            if sync:
                response = self.wait_for_json_response("hss")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def delete_wounded(self, wod_id, amount, sync=True, quiet=False):
        try:
            self.send_json_command("hdu", {
                "U": wod_id,
                "A": amount
            })
            if sync:
                response = self.wait_for_json_response("hdu")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def heal_all(self, max_cost, sync=True, quiet=False):
        try:
            self.send_json_command("hra", {
                "C2": max_cost
            })
            if sync:
                response = self.wait_for_json_response("hra")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False


    def ask_alliance_help_heal(self, package_id, sync=True, quiet=False):
        try:
            self.send_json_command("ahr", {
                "ID": package_id,
                "T": 2
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
