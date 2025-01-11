from ..base_socket import BaseSocket

class Friends(BaseSocket):
    def get_friends(self, sync=True, quiet=False):
        try:
            self.send_json_command("gfc", {})
            if sync:
                response = self.wait_for_json_response("gfc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def send_email(self, sender_name, target_name, target_email, message, sync=True, quiet=False):
        try:
            self.send_json_command("sem", {
                "SN": sender_name,
                "TN": target_name,
                "EM": target_email,
                "TXT": message
            })
            if sync:
                response = self.wait_for_json_response("sem")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
