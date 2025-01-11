from ..base_socket import BaseSocket
import time

class Buildings(BaseSocket):
    def build(self, wod_id, x, y, rotated=0, sync=True, quiet=False):
        try:
            self.send_json_command("ebu", {
                "WID": wod_id,
                "X": x,
                "Y": y,
                "R": rotated,
                "PWR": 0,
                "PO": -1,
                "DOID": -1
            })
            if sync:
                response = self.wait_for_json_response("ebu")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def upgrade_building(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("eup", {
                "OID": building_id,
                "PWR": 0,
                "PO": -1
            })
            if sync:
                response = self.wait_for_json_response("eup")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def move_building(self, wod_id, x, y, rotated=0, sync=True, quiet=False):
        try:
            self.send_json_command("emo", {
                "OID": wod_id,
                "X": x,
                "Y": y,
                "R": rotated
            })
            if sync:
                response = self.wait_for_json_response("emo")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def sell_building(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("sbd", {
                "OID": building_id
            })
            if sync:
                response = self.wait_for_json_response("sbd")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
        
    def destroy_building(self, building_id, sync=True, quiet=False):
        try:
            self.send_json_command("edo", {
                "OID": building_id
            })
            if sync:
                response = self.wait_for_json_response("edo")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False

    def skip_construction(self, building_id, free_skip=1, sync=True, quiet=False):
        try:
            self.send_json_command("fco", {
                "OID": building_id,
                "FS": free_skip
            })
            if sync:
                response = self.wait_for_json_response("fco")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def time_skip_construction(self, building_id, time_skip_type, sync=True, quiet=False):
        try:
            self.send_json_command("msb", {
                "OID": building_id,
                "MST": time_skip_type
            })
            if sync:
                response = self.wait_for_json_response("msb")
                self.raise_for_status(response)
                return response
            return True
        except Exception as e:
            if not quiet:
                raise e
            return False
    
    def wait_finish_construction(self, building_id, timeout=5, quiet=False):
        try:
            response = self.wait_for_json_response("fbe", {
                "OID": building_id
            }, timeout=timeout)
            self.raise_for_status(response)
            return response
        except Exception as e:
            if not quiet:
                raise e
            return False

    def instant_build(self, building_id, wod_id, x, y, rotated=0, time_skips=None, cooldown=0, free_skip=1, sync=True, quiet=False):
        self.build(wod_id, x, y, rotated, sync=sync, quiet=quiet)
        for skip in (time_skips or []):
            self.time_skip_construction(building_id, skip, sync=sync, quiet=quiet)
        time.sleep(cooldown)
        self.skip_construction(building_id, free_skip, sync=sync, quiet=quiet)
        if sync:
            self.wait_finish_construction(building_id, quiet=quiet)

    def instant_upgrade(self, building_id, time_skips=None, cooldown=0, free_skip=1, sync=True, quiet=False):
        self.upgrade_building(building_id, sync=sync, quiet=quiet)
        for skip in (time_skips or []):
            self.time_skip_construction(building_id, skip, sync=sync, quiet=quiet)
        time.sleep(cooldown)
        self.skip_construction(building_id, free_skip, sync=sync, quiet=quiet)
        if sync:
            self.wait_finish_construction(building_id, quiet=quiet)
    
    def instant_destroy(self, building_id, time_skips=None, cooldown=0, free_skip=1, sync=True, quiet=False):
        self.destroy_building(building_id, sync=sync, quiet=quiet)
        for skip in (time_skips or []):
            self.time_skip_construction(building_id, skip, sync=sync, quiet=quiet)
        time.sleep(cooldown)
        self.skip_construction(building_id, free_skip, sync=sync, quiet=quiet)
