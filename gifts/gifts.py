from ..base_socket import BaseSocket

class Gifts(BaseSocket):
    def send_gift(self, target_id, package_type, amount, sync=True, quiet=False):
        try:
            self.send_json_command("gpg", {
                "PID": package_type,
                "RID": target_id,
                "A": amount
            })
            if sync:
                response = self.wait_for_json_response("gpg")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
