from ..base_gge_socket import BaseGgeSocket

class SpecialOffers(BaseGgeSocket):
    def buy_special_offer(self, offer_id, package_ids=[0], sync=True, quiet=False):
        try:
            self.send_json_command("oop", {
                "OID": offer_id,
                "C": 1,
                "ODI": package_ids
            })
            if sync:
                response = self.wait_for_json_response("oop")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def collect_special_offer_gift(self, gift_id, sync=True, quiet=False):
        try:
            self.send_json_command("oop", {
                "OID": gift_id,
                "C": 1,
                "ODI": [0]
            })
            if sync:
                response = self.wait_for_json_response("oop")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False




def buy_special_offer(ws, offer_id, package_ids=[0]):
    ws.send(f"""%xt%EmpireEx_3%oop%1%{{"OID":{offer_id},"C":1,"ODI":{package_ids}}}""")
