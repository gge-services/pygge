from ..base_socket import BaseSocket

class OuterRealms(BaseSocket):
    def get_outer_realms_points(self, sync=True, quiet=False):
        try:
            self.send_json_command("tsh", {})
            if sync:
                response = self.wait_for_json_response("tsh")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False


    def choose_outer_realm_castle(self, castle_id, premium=0, sync=True, quiet=False):
        try:
            self.send_json_command("tsc", {
                "ID": castle_id,
                "OC2": premium,
                "PWR": premium,
                "GST": 2
            })
            if sync:
                response = self.wait_for_json_response("tsc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def get_outer_realm_token(self, sync=True, quiet=False):
        try:
            self.send_json_command("glt", {
                "GST": 2
            })
            if sync:
                response = self.wait_for_json_response("glt")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def login_outer_realm(self, token, sync=True, quiet=False):
        try:
            self.send_json_command("tlep", {
                "TLT": token
            })
            if sync:
                response = self.wait_for_json_response("lli")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False