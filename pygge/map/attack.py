from ..base_gge_socket import BaseGgeSocket

class Attack(BaseGgeSocket):
    def send_attack(self, kingdom, sx, sy, tx, ty, army, lord_id=0, horses_type=-1, feathers=0, slowdown=0, boosters=[], support_tools=[], final_wave=[], sync=True, quiet=False):
        try:
            self.send_json_command("cra", {
                "SX": sx,
                "SY": sy,
                "TX": tx,
                "TY": ty,
                "KID": kingdom,
                "LID": lord_id,
                "WT": 0,
                "HBW": horses_type,
                "BPC": 0,
                "ATT": 0,
                "AV": 0,
                "LP": 0,
                "FC": 0,
                "PTT": feathers,
                "SD": slowdown,
                "ICA": 0,
                "CD": 99,
                "A": army,
                "BKS": boosters,
                "AST": support_tools,
                "RW": final_wave,
                "ASCT": 0
            })
            if sync:
                response = self.wait_for_json_response("cra")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
