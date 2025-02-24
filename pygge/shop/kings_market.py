from ..base_gge_socket import BaseGgeSocket

class KingsMarket(BaseGgeSocket):
    def buy_king_banner(self, sync=True, quiet=False):
        try:
            self.send_json_command("gbp", {})
            if sync:
                response = self.wait_for_json_response("gbp")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def start_protection(self, duration, sync=True, quiet=False):
        # duration: 0 = 7d, 1 = 14d, 2 = 21d, 3 = 60d
        try:
            self.send_json_command("mps", {
                "CD": duration
            })
            if sync:
                response = self.wait_for_json_response("mps")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def buy_production_slot(self, queue_type, sync=True, quiet=False):
        # queue_type: 0 = Barracks, 1 = Workshop
        try:
            self.send_json_command("ups", {
                "LID": queue_type
            })
            if sync:
                response = self.wait_for_json_response("ups")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def open_gates(self, kingdom, castle_id, duration=0, sync=True, quiet=False):
        # duration: 0 = 6h, 1 = 12h
        try:
            self.send_json_command("mos", {
                "CID": castle_id,
                "KID": kingdom,
                "CD": duration
            })
            if sync:
                response = self.wait_for_json_response("mos")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def buy_feast(self, kingdom, castle_id, feast_type, sync=True, quiet=False):
        # feast_type: 0-9
        try:
            self.send_json_command("bfs", {
                "CID": castle_id,
                "KID": kingdom,
                "T": feast_type,
                "PO": -1,
                "PWR": 0
            })
            if sync:
                response = self.wait_for_json_response("bfs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        