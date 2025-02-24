from ..base_gge_socket import BaseGgeSocket

class CastleGifts(BaseGgeSocket):
    def collect_citizen_gift(self, sync=True, quiet=False):
        try:
            self.send_json_command("irc", {})
            if sync:
                response = self.wait_for_json_response("irc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def collect_citizen_quest(self, choice, sync=True, quiet=False):
        # choice: 0 or 1
        try:
            self.send_json_command("jjc", {
                "CO": choice
            })
            if sync:
                response = self.wait_for_json_response("jjc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def collect_ressource_gift(self, resource_type, sync=True, quiet=False):
        # resource_type: 0 = wood, 1 = stone, 2 = food
        try:
            self.send_json_command("rcc", {
                "RT": resource_type
            })
            if sync:
                response = self.wait_for_json_response("rcc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
