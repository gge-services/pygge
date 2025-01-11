from ..base_socket import BaseSocket

class LuckyWheel(BaseSocket):
    def switch_lucky_wheel_mode(self, sync=True, quiet=False):
        try:
            self.send_json_command("lwm", {})
            if sync:
                response = self.wait_for_json_response("lwm")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def spin_lucky_wheel(self, wheel_type, sync=True, quiet=False):
        try:
            self.send_json_command("lws", {
                "LWET": wheel_type
            })
            if sync:
                response = self.wait_for_json_response("lws")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def spin_classic_lucky_wheel(self, sync=True, quiet=False):
        return self.spin_lucky_wheel(0, sync, quiet)
        
    def spin_paid_lucky_wheel(self, sync=True, quiet=False):
        return self.spin_lucky_wheel(1, sync, quiet)
