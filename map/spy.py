from ..base_socket import BaseSocket

class Spy(BaseSocket):
    def send_spy(self, kingdom, source_id, tx, ty, spy_count=1, precision=50, spy_type=0, horses_type=-1, feathers=0, slowdown=0, sync=True, quiet=False):
        try:
            self.send_json_command("csm", {
                "SID": source_id,
                "TX": tx,
                "TY": ty,
                "SC": spy_count,
                "ST": spy_type,
                "SE": precision,
                "HBW": horses_type,
                "KID": kingdom,
                "PTT": feathers,
                "SD": slowdown
            })
            if sync:
                response = self.wait_for_json_response("csm")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
