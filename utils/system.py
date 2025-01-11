from ..base_socket import BaseSocket

class System(BaseSocket):
    def ver_check(self, sync=True, quiet=False):
        try:
            self.send_xml_message("sys", "verChk", "0", "<ver v='166' />")
            if sync:
                response = self.wait_for_xml_response("sys", "apiOK", "0")
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def join_server(self, sync=True, quiet=False):
        try:
            self.send_xml_message("sys", "login", "0", f"<login z='{self.server_header}'><nick><![CDATA[]]></nick><pword><![CDATA[1065004%fr%0]]></pword></login>")
            if sync:
                response = self.wait_for_json_response("nfo")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def auto_join(self, sync=True, quiet=False):
        try:
            self.send_xml_message("sys", "autoJoin", "-1", "")
            if sync:
                response = self.wait_for_xml_response("sys", "joinOK", "1")
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def round_trip(self, sync=True, quiet=False):
        try:
            self.send_xml_message("sys", "roundTrip", "1", "")
            if sync:
                response = self.wait_for_xml_response("sys", "roundTripRes", "1")
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def vck(self, build_number, sync=True, quiet=False):
        try:
            self.send_raw_command("vck", [build_number, "web-html5", "<RoundHouseKick>"])
            if sync:
                response = self.wait_for_json_response("vck")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def ping(self, quiet=False):
        try:
            self.send_raw_command("pin", ["<RoundHouseKick>"])
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def init_socket(self, sync=True, quiet=False):
        self.opened.wait()
        self.ver_check(sync=sync, quiet=quiet)
        self.join_server(sync=sync, quiet=quiet)
        self.auto_join(sync=sync, quiet=quiet)
        self.round_trip(sync=sync, quiet=quiet)

    def keep_alive(self, quiet=False):
        self.opened.wait()
        while self.opened.is_set():
            closed = self.closed.wait(60)
            if not closed:
                self.ping(quiet=quiet)
