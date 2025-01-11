from ..base_socket import BaseSocket

class Settings(BaseSocket):
    def show_animations(self, show=True, sync=True, quiet=False):
        try:
            self.send_json_command("ani", {
                "ANI": show
            })
            if sync:
                response = self.wait_for_json_response("ani")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def show_small_attacks(self, show=True, sync=True, quiet=False):
        try:
            self.send_json_command("mvf", {
                "FID": 0,
                "ACT": not show
            })
            if sync:
                response = self.wait_for_json_response("mvf")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def show_small_attacks_alliance(self, show=True, sync=True, quiet=False):
        try:
            self.send_json_command("mvf", {
                "FID": 1,
                "ACT": not show
            })
            if sync:
                response = self.wait_for_json_response("mvf")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def show_resource_carts(self, show=True, sync=True, quiet=False):
        try:
            self.send_json_command("mvf", {
                "FID": 2,
                "ACT": not show
            })
            if sync:
                response = self.wait_for_json_response("mvf")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def set_misc_settings(self, show_vip_banners=1, offline_for_friends=0, ruby_purchase_confirmation_thr=-1, sync=True, quiet=False):
        try:
            self.send_json_command("opt", {
                "SVF": show_vip_banners,
                "OFF": offline_for_friends,
                "CC2T": ruby_purchase_confirmation_thr
            })
            if sync:
                response = self.wait_for_json_response("opt")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def set_hospital_settings(self, kingdom, castle_id, accept_ruby_units=-1, sync=True, quiet=False):
        try:
            self.send_json_command("hfl", {
                "KID": kingdom,
                "AID": castle_id,
                "HRF": accept_ruby_units
            })
            if sync:
                response = self.wait_for_json_response("hfl")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False