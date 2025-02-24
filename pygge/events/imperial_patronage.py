from ..base_gge_socket import BaseGgeSocket

class ImperialPatronage(BaseGgeSocket):
    def open_imperail_patronage(self, sync=True, quiet=False):
        try:
            self.send_json_command("gdti", {})
            if sync:
                response = self.wait_for_json_response("gdti")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def give_imperial_patronage(self, devise_id, amount, sync=True, quiet=False):
        # devise_id: 31 = construction token, 32 = sceats, 33 = amelioration token, 34 = daimyo token, 35 = samurai token, 36 = khan token, 37 = khan tablet
        # devise_id (premium): 38 = imperial patronage scroll, 39 = construction token, 40 = sceats, 41 = amelioration token, 42 = daimyo token, 43 = samurai token, 44 = khan token, 45 = khan tablet
        try:
            self.send_json_command("ddi", {
                "DIV": [{
                    "DII": devise_id, "DIA": amount
                }]
            })
            if sync:
                response = self.wait_for_json_response("ddi")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
