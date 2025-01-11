from ..base_socket import BaseSocket

class GlobalEffects(BaseSocket):
    def get_global_effects(self, sync=True, quiet=False):
        try:
            self.send_json_command("usg", {})
            if sync:
                response = self.wait_for_json_response("usg")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def upgrade_global_effect(self, effect_id, sync=True, quiet=False):
        try:
            self.send_json_command("agb", {
                "GEID": effect_id
            })
            if sync:
                response = self.wait_for_json_response("agb")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
