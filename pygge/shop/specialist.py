from ..base_gge_socket import BaseGgeSocket

class Specialist(BaseGgeSocket):
    def buy_market_carts(self, sync=True, quiet=False):
        try:
            self.send_json_command("bcs", {
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("bcs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def buy_marauder(self, sync=True, quiet=False):
        try:
            self.send_json_command("bms", {
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("bms")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def buy_overseer(self, resource_type, sync=True, quiet=False):
        # resource_type: 0 = Wood, 1 = Stone, 2 = Food, ??? = honey, ??? = mead
        try:
            self.send_json_command("bos", {
                "T": resource_type,
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("bos")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def buy_travel_maps(self, sync=True, quiet=False):
        try:
            self.send_json_command("brs", {
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("brs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def buy_tax_collector(self, sync=True, quiet=False):
        try:
            self.send_json_command("btx", {
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("btx")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def buy_drill_instructor(self, sync=True, quiet=False):
        try:
            self.send_json_command("bis", {
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("bis")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False