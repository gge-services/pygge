from ..base_socket import BaseSocket
import requests

class Auth(BaseSocket):
    def check_username_availability(self, name, sync=True, quiet=False):
        try:
            self.send_json_command("vln", {
                "NOM": name
            })
            if sync:
                response = self.wait_for_json_response("vln")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def check_user_exists(self, name, sync=True, quiet=False):
        try:
            self.send_json_command("vln", {
                "NOM": name
            })
            if sync:
                response = self.wait_for_json_response("vln")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def register(self, username, password, email):
        server_index = self.server_header.split("EmpireEx_")[1] if "EmpireEx_" in self.server_header else "1"
        request = requests.get(f"https://lp2.goodgamestudios.com/register/index.json?gameId=12&networkId=1&COUNTRY=FR&forceGeoip=false&forceInstance=true&PN={username}&LANG=fr-FR&MAIL={email}&PW={password}&AID=0&adgr=0&adID=0&camp=0&cid=&journeyHash=1720629282364650193&keyword=&matchtype=&network=&nid=0&placement=&REF=&tid=&timeZone=14&V=&campainPId=0&campainCr=0&campainLP=0&DID=0&websiteId=380635&gci=0&adClickId=&instance={server_index}")
        request.raise_for_status()
        response = request.json()
        if not response["res"] or response["err"]:
            raise Exception(f"Failed to register: {response['err']}")
        return response

    def login(self, name, password, sync=True, quiet=False):
        try:
            self.send_json_command("lli", {
                "CONM": 175,
                "RTM": 24,
                "ID": 0,
                "PL": 1,
                "NOM": name,
                "PW": password,
                "LT": None,
                "LANG": "fr",
                "DID": "0",
                "AID": "1674256959939529708",
                "KID": "",
                "REF": "https://empire.goodgamestudios.com",
                "GCI": "",
                "SID": 9,
                "PLFID": 1
            })
            if sync:
                response = self.wait_for_json_response("lli")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def login_facebook(self, facebook_id, facebook_token, facebook_account_id, sync=True, quiet=False):
        try:
            self.send_json_command("lli", {
                "CONM": 175,
                "RTM": 24,
                "ID": 0,
                "PL": 1,
                "NOM": "null",
                "PW": "null",
                "LT": None,
                "LANG": "fr",
                "DID": "0",
                "AID": "1674256959939529708",
                "KID": "",
                "REF": "https://empire.goodgamestudios.com",
                "GCI": "",
                "SID": 9,
                "PLFID": 1,
                "FID": facebook_id,
                "FTK": facebook_token,
                "FAID": facebook_account_id
            })
            if sync:
                response = self.wait_for_json_response("lli")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def ask_password_recovery(self, email, sync=True, quiet=False):
        try:
            self.send_json_command("lpp", {
                "MAIL": email
            })
            if sync:
                response = self.wait_for_json_response("lpp")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
