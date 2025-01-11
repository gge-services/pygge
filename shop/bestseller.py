from ..base_socket import BaseSocket

class Bestseller(BaseSocket):
    def buy_from_bestseller(self, bestseller_id, package_type, amount, sync=True, quiet=False):
        try:
            self.send_json_command("bso", {
                "OID": package_type,
                "AMT": amount,
                "POID": bestseller_id
            })
            if sync:
                response = self.wait_for_json_response("bso")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
