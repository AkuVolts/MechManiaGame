from enum import Enum
from game.stat_set import StatSet

class ItemModel():
    def __init__(self, stat_set, item_timer, cost) -> None:
        self.stat_set = stat_set
        self.item_timer = item_timer
        self.cost = cost

class Item(Enum):

    #Misc
    SHIELD = ItemModel(StatSet(0,0,0,0), 1,8)

    #Damage Items
    PROCRUSTEAN_IRON = ItemModel(StatSet(0, 0, 0, 0), -1, 8)
    STRENGTH_POTION = ItemModel(StatSet(0, 4, 0, 0), 1, 5)
    RALLY_BANNER = ItemModel(StatSet(0,2,0,0), -1, 8)

    #Speed Items
    ANEMOI_WINGS = ItemModel(StatSet(0, 0, 1, 0), -1, 8)
    SPEED_POTION = ItemModel(StatSet(0, 0, 2, 0), 1, 5)

    #Range Items
    DEXTERITY_POTION = ItemModel(StatSet(0, 0, 0, 2), 1, 5)
    HUNTING_SCOPE = ItemModel(StatSet(0,0,0,1), -1, 8)

    #Chenge Items
    HEAVY_BROADSWORD = ItemModel(StatSet(0, 0, 0, 0), 0, 10) #Change to knight
    MAGIC_STAFF = ItemModel(StatSet(0, 0, 0, 0), 0, 10) #Change to Wizard
    STEEL_TIPPED_ARROW = ItemModel(StatSet(0, 0, 0, 0), 0, 10) #Change to archer
    
    
    
    
    NONE = ItemModel(StatSet(0, 0, 0, 0), -1, 100)

