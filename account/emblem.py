from ..base_socket import BaseSocket

class Emblem(BaseSocket):
    def change_emblem(self, bg_type, bg_color_1, bg_color_2, icons_type, icon_id_1, icon_color_1, icon_id_2, icon_color_2, sync=True, quiet=False):
        try:
            self.send_json_command("cem", {
                "CAE": {
                    "BGT": bg_type,
                    "BGC1": bg_color_1,
                    "BGC2": bg_color_2,
                    "SPT": icons_type,
                    "S1": icon_id_1,
                    "SC1": icon_color_1,
                    "S2": icon_id_2,
                    "SC2": icon_color_2
                }
            })
            if sync:
                response = self.wait_for_json_response("cem")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
