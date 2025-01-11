from ..base_socket import BaseSocket

class Castle(BaseSocket):
    def get_castles(self, sync=True, quiet=False):
        try:
            self.send_json_command("gcl", {})
            if sync:
                response = self.wait_for_json_response("gcl")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def get_detailed_castles(self, sync=True, quiet=False):
        try:
            self.send_json_command("dcl", {})
            if sync:
                response = self.wait_for_json_response("dcl")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def go_to_castle(self, kingdom, castle_id=-1, sync=True, quiet=False):
        try:
            self.send_json_command("jca", {
                "CID": castle_id,
                "KID": kingdom
            })
            if sync:
                response = self.wait_for_json_response("jaa")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def rename_castle(self, kingdom, castle_id, castle_type, name, paid=0, sync=True, quiet=False):
        try:
            self.send_json_command("arc", {
                "CID": castle_id,
                "P": paid,
                "KID": kingdom,
                "AT": castle_type,
                "N": name
            })
            if sync:
                response = self.wait_for_json_response("arc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def rename_castle_with_cc2t(self, kingdom, castle_id, castle_type, name, cost, sync=True, quiet=False):
        try:
            self.send_json_command("arc", {
                "CID": castle_id,
                "P": 1,
                "KID": kingdom,
                "AT": castle_type,
                "N": name,
                "cmdID": "arc",
                "CC2T": cost
            })
            if sync:
                response = self.wait_for_json_response("arc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def relocate_main_castle(self, x, y, sync=True, quiet=False):
        try:
            self.send_json_command("rco", {
                "PX": x,
                "PY": y
            })
            if sync:
                response = self.wait_for_json_response("rco")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def first_relocate_main_castle(self, x, y, sync=True, quiet=False):
        try:
            self.send_json_command("rst", {
                "PX": x,
                "PY": y
            })
            if sync:
                response = self.wait_for_json_response("rst")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
