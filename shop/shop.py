from ..base_socket import BaseSocket

class Shop(BaseSocket):
        def buy_package_generic(self, kingdom, shop_type, shop_id, package_id, amount, sync=True, quiet=False):
            try:
                self.send_json_command("sbp", {
                    "PID": package_id,
                    "BT": shop_type,
                    "TID": shop_id,
                    "AMT": amount,
                    "KID": kingdom,
                    "AID": -1,
                    "PC2": -1,
                    "BA": 0,
                    "PWR": 0,
                    "_PO": -1
                })
                if sync:
                    response = self.wait_for_json_response("sbp")
                    self.raise_for_status(response)
                    return response
                return True
            except Exception as e:
                if not quiet:
                    raise e
                return False

        def buy_vip_time(self, kingdom, package_id, amount, sync=True, quiet=False):
            # package_type: 170 = 1d, 171 = 7d, 172 = 30d
            return self.buy_package_generic(kingdom, 2, -1, package_id, amount, sync, quiet)
        
        def buy_vip_points(self, kingdom, package_id, amount, sync=True, quiet=False):
            # package_type: 167 = 300, 168 = 1500, 169 = 4500
            return self.buy_package_generic(kingdom, 2, -1, package_id, amount, sync, quiet)
        
        def buy_from_master_blacksmith(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 116, package_id, amount, sync, quiet)
        
        def buy_from_nomad_shop(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 94, package_id, amount, sync, quiet)
        
        def buy_from_nomad_armorer(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 49, package_id, amount, sync, quiet)
        
        def buy_from_traveling_merchant(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 22, package_id, amount, sync, quiet)
        
        def buy_from_armorer(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 27, package_id, amount, sync, quiet)
        
        def buy_from_blacksmith(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 101, package_id, amount, sync, quiet)
        
        def buy_from_gift_seller(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 66, package_id, amount, sync, quiet)
        
        def buy_from_blade_coast_shop(self, kingdom, package_id, amount, sync=True, quiet=False):
            return self.buy_package_generic(kingdom, 0, 4, package_id, amount, sync, quiet)
        
        def set_buying_castle(self, castle_id, kingdom=0, sync=True, quiet=False):
            try:
                self.send_json_command("gbc", {
                    "CID": castle_id,
                    "KID": kingdom
                })
                if sync:
                    response = self.wait_for_json_response("gbc")
                    self.raise_for_status(response)
                    return response
                return True
            except Exception as e:
                if not quiet:
                    raise e
                return False
