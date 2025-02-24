from ..base_gge_socket import BaseGgeSocket

class Ruins(BaseGgeSocket):
    def get_ruin_infos(self, x, y, sync=True, quiet=False):
        try:
            self.send_json_command("rui", {
                "PX": x,
                "PY": y
            })
            if sync:
                response = self.wait_for_json_response("rui")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def ask_ruin_infos_message(self, x, y, sync=True, quiet=False):
        try:
            self.send_json_command("rmb", {
                "PX": x,
                "PY": y
            })
            if sync:
                response = self.wait_for_json_response("rmb")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
