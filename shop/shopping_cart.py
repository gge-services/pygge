from ..base_socket import BaseSocket

class ShoppingCart(BaseSocket):
    def edit_shopping_cart(self, packages_left=[], packages_middle=[], packages_right=[], sync=True, quiet=False):
        try:
            self.send_json_command("ssc", {
                "IGC": 0,
                "SCA": packages_left,
                "SCB": packages_middle,
                "SCC": packages_right
            })
            if sync:
                response = self.wait_for_json_response("ssc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
