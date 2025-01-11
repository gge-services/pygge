from ..base_socket import BaseSocket

class Account(BaseSocket):
    def get_account_infos(self, sync=True, quiet=False):
        try:
            self.send_json_command("gpi", {})
            if sync:
                response = self.wait_for_json_response("gpi")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def register_email(self, email, subscribe=False, sync=True, quiet=False):
        try:
            self.send_json_command("vpm", {
                "MAIL": email,
                "NEWSLETTER": subscribe
            })
            if sync:
                response = self.wait_for_json_response("vpm")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def get_username_change_infos(self, sync=True, quiet=False):
        try:
            self.send_json_command("gnci", {})
            if sync:
                response = self.wait_for_json_response("gnci")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def change_username(self, new_username, sync=True, quiet=False):
        try:
            self.send_json_command("cpne", {
                "PN": new_username
            })
            if sync:
                response = self.wait_for_json_response("cpne")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def change_password(self, old_password, new_password, sync=True, quiet=False):
        try:
            self.send_json_command("scp", {
                "OPW": old_password,
                "NPW": new_password
            })
            if sync:
                response = self.wait_for_json_response("scp")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def ask_email_change(self, new_email, sync=True, quiet=False):
        try:
            self.send_json_command("rmc", {
                "PMA": new_email
            })
            if sync:
                response = self.wait_for_json_response("rmc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def get_email_change_status(self, sync=True, quiet=False):
        try:
            self.send_json_command("mns", {})
            if sync:
                response = self.wait_for_json_response("mns")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def cancel_email_change(self, sync=True, quiet=False):
        try:
            self.send_json_command("cmc", {})
            if sync:
                response = self.wait_for_json_response("cmc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def activate_facebook_connection(self, facebook_id, facebook_token, facebook_account_id, activate=True, sync=True, quiet=False):
        try:

            self.send_json_command("fcs", {
                "SFC": activate,
                "FID": facebook_id,
                "FTK": facebook_token,
                "FAID": facebook_account_id
            })
            if sync:
                response = self.wait_for_json_response("fcs")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False