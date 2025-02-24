from ..base_gge_socket import BaseGgeSocket

class Tax(BaseGgeSocket):
    def get_tax_infos(self, sync=True, quiet=False):
        try:
            self.send_json_command("txi", {})
            if sync:
                response = self.wait_for_json_response("txi")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def start_tax(self, tax_type, sync=True, quiet=False):
        try:
            self.send_json_command("txs", {
                "TT": tax_type,
                "TX": 3
            })
            if sync:
                response = self.wait_for_json_response("txs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def collect_tax(self, sync=True, quiet=False):
        try:
            self.send_json_command("txc", {
                "TR": 29
            })
            if sync:
                response = self.wait_for_json_response("txc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
