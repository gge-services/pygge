from ..base_gge_socket import BaseGgeSocket

class BuildItems(BaseGgeSocket):
    def equip_build_item(self, kingdom_id, castle_id, building_id, slot_id, item_id, sync=True, quiet=False):
        try:
            self.send_json_command("rpc", {
                "OID": building_id,
                "CID": item_id,
                "SID": slot_id,
                "M": 0,
                "KID": kingdom_id,
                "AID": castle_id
            })
            if sync:
                response = self.wait_for_json_response("rpc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
