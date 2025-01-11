from ..base_socket import BaseSocket

class Defense(BaseSocket):
    def get_castle_defense_complete(self, x, y, castle_id, sync=True, quiet=False):
        try:
            self.send_json_command("dfc", {
                "CX": x,
                "CY": y,
                "AID": castle_id,
                "KID": -1,
                "SSV": 0
            })
            if sync:
                response = self.wait_for_json_response("dfc")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def change_defense_keep(self, x, y, castle_id, min_units_to_consume_tools, melee_percentage, tools, support_tools, sync=True, quiet=False):
        try:
            self.send_json_command("dfk", {
                "CX": x,
                "CY": y,
                "AID": castle_id,
                "MAUCT": min_units_to_consume_tools,
                "UC": melee_percentage,
                "S": tools,
                "STS": support_tools
            })
            if sync:
                response = self.wait_for_json_response("dfk")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def change_defense_wall(self, x, y, castle_id, left_tools, left_unit_percentage, left_melee_percentage, middle_tools, middle_unit_percentage, middle_melee_percentage, right_tools, right_unit_percentage, right_melee_percentage, sync=True, quiet=False):
        try:
            self.send_json_command("dfw", {
                "CX": x,
                "CY": y,
                "AID": castle_id,
                "L": {
                    "S": left_tools,
                    "UP": left_unit_percentage,
                    "UC": left_melee_percentage
                },
                "M": {
                    "S": middle_tools,
                    "UP": middle_unit_percentage,
                    "UC": middle_melee_percentage
                },
                "R": {
                    "S": right_tools,
                    "UP": right_unit_percentage,
                    "UC": right_melee_percentage
                }
            })
            if sync:
                response = self.wait_for_json_response("dfw")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def change_defense_moat(self, x, y, castle_id, left_tools, middle_tools, right_tools, sync=True, quiet=False):
        try:
            self.send_json_command("dfm", {
                "CX": x,
                "CY": y,
                "AID": castle_id,
                "LS": left_tools,
                "MS": middle_tools,
                "RS": right_tools
            })
            if sync:
                response = self.wait_for_json_response("dfm")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
