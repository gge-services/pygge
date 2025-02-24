from ..base_gge_socket import BaseGgeSocket

class Map(BaseGgeSocket):
    def get_map_chunk(self, kingdom, x, y, sync=True, quiet=False):
        try:
            self.send_json_command("gaa", {
                "KID": kingdom,
                "AX1": x,
                "AY1": y,
                "AX2": x + 12,
                "AY2": y + 12
            })
            if sync:
                response = self.wait_for_json_response("gaa")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def get_closest_npc(self, kingdom, npc_type, min_level=1, max_level=-1, owner_id=-1, sync=True, quiet=False):
        try:
            self.send_json_command("fnm", {
                "T": npc_type,
                "KID": kingdom,
                "LMIN": min_level,
                "LMAX": max_level,
                "NID": owner_id
            })
            if sync:
                response = self.wait_for_json_response("fnm")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def get_target_infos(self, kingdom, sx, sy, tx, ty, sync=True, quiet=False):
        try:
            self.send_json_command("adi", {
                "SX": sx,
                "SY": sy,
                "TX": tx,
                "TY": ty,
                "KID": kingdom
            })
            if sync:
                response = self.wait_for_json_response("adi")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
