from .account.account import Account
from .account.auth import Auth
from .account.emblem import Emblem
from .account.friends import Friends
from .account.settings import Settings

from .alliance.help import Help

from .army.hospital import Hospital
from .army.soldiers import Soldiers
from .army.tools import Tools
from .army.units import Units

from .building.buildings_inventory import BuildingsInventory
from .building.buildings import Buildings
from .building.extension import Extension
from .building.repair import Repair
from .building.wall import Wall

from .castle.castle import Castle
from .castle.defense import Defense

from .events.beyond_the_horizon import BeyondTheHorizon
from .events.events import Events
from .events.imperial_patronage import ImperialPatronage
from .events.lucky_wheel import LuckyWheel
from .events.mercenary_camp import MercenaryCamp
from .events.outer_realms import OuterRealms
from .events.technicus import Technicus
from .events.wishing_well import WishingWell

from .generals.tavern import Tavern

from .gifts.castle_gifts import CastleGifts
from .gifts.daily_gifts import DailyGifts
from .gifts.gifts import Gifts

from .lords.lords import Lords

from .map.attack import Attack
from .map.bookmarks import Bookmarks
from .map.map import Map
from .map.ruins import Ruins
from .map.spy import Spy

from .shop.bestseller import Bestseller
from .shop.kings_market import KingsMarket
from .shop.shop import Shop
from .shop.shopping_cart import ShoppingCart
from .shop.special_offers import SpecialOffers
from .shop.specialist import Specialist

from .tutorial.tutorial import Tutorial

from .utils.system import System

from .misc.build_items import BuildItems
from .misc.global_effects import GlobalEffects
from .misc.quests import Quests
from .misc.tax import Tax

class GgeSocket(
        Account, Auth, Emblem, Friends, Settings,
        Help,
        Hospital, Soldiers, Tools, Units,
        BuildingsInventory, Buildings, Extension, Repair, Wall,
        Castle, Defense,
        BeyondTheHorizon, Events, ImperialPatronage, LuckyWheel, MercenaryCamp, OuterRealms, Technicus, WishingWell,
        Tavern,
        CastleGifts, DailyGifts, Gifts,
        Lords,
        Attack, Bookmarks, Map, Ruins, Spy,
        Bestseller, KingsMarket, Shop, ShoppingCart, SpecialOffers, Specialist,
        Tutorial,
        System,
        BuildItems, GlobalEffects, Quests, Tax
    ):

    def open_quest_book(self, sync=True, quiet=False):
        self.tracking_recommended_quests(quiet=quiet)
        self.get_quests(sync=sync, quiet=quiet)
    
    def open_tax_menu(self, sync=True, quiet=False):
        self.get_tax_infos(sync=sync, quiet=quiet)
        self.get_tax_infos(sync=sync, quiet=quiet)

    def open_defense_menu(self, x, y, castle_id, sync=True, quiet=False):
        self.get_castle_defense_complete(x, y, castle_id, sync=sync, quiet=quiet)
        self.get_lords(sync=sync, quiet=quiet)
    
    def close_defense_menu(self, sync=True, quiet=False):
        self.get_units_inventory(sync=sync, quiet=quiet)

    def open_construction_menu(self, sync=True, quiet=False):
        self.get_building_inventory(sync=sync, quiet=quiet)

    def open_barracks(self, sync=True, quiet=False):
        self.get_detailed_castles(sync=sync, quiet=quiet)
        self.get_recruitment_queue(sync=sync, quiet=quiet)
        self.get_units_inventory(sync=sync, quiet=quiet)
    
    def open_workshop(self, sync=True, quiet=False):
        self.get_detailed_castles(sync=sync, quiet=quiet)
        self.get_production_queue(sync=sync, quiet=quiet)
        self.get_units_inventory(sync=sync, quiet=quiet)

    def open_hospital(self, sync=True, quiet=False):
        self.get_detailed_castles(sync=sync, quiet=quiet)

    def open_map(self, kingdom, sync=True, quiet=False):
        self.get_bookmarks(sync=sync, quiet=quiet)
        self.get_map_chunk(kingdom, 0, 0, sync=sync, quiet=quiet)

    def skip_generals_tutorial(self, sync=True, quiet=False):
        self.get_offerings_status(sync=sync, quiet=quiet)
        self.complete_quest_condition(1, "visitGeneralsInn", sync=sync, quiet=quiet)
        self.skip_generals_intro(sync=sync, quiet=quiet)
