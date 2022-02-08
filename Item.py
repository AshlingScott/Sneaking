from abc import *
from Alter import *

# Items that charcters equip
# Often apply alters
class Item(ABC):
    # The list of all the alters an item provides
    alters = []

    # Removes the item from the unit, removing alters with this as source
    def destroy(self):
        for x in range(len(self.owner.alters)):
            if (self.owner.alters[x].source == self):
                self.owner.alters.pop(x)

# Boots give the unit +2 to movement
class Boots(Item):
    def __init__(self, owner: Unit):
        self.owner = owner
        self.name = "Boots of Speed"
        self.description = "Gives the Unit +2 to movement"
        self.alters.append(Speed(True, 0, True, owner, 2, self))

class Spyglass(Item):
    def __init__(self, owner: Unit):
        self.owner = owner
        self.name = "Spyglass"
        self.description = "Gives the Unit +2 to vision"
        self.alters.append(Vision(True, 0, True, owner, 2, self))

class Power_Well(Item):
    def __init__(self, owner: Unit):
        self.owner = owner
        self.name = "Power_Well"
        self.description = "Grants +5 maximum energy to the Unit"
        self.alters.append(Energy(True, 0, True, 5, self))

class Energy_Charm(Item):
    def __init__(self, owner: Unit):
        self.owner = owner
        self.name = "Energy Charm"
        self.description = "Gives the Unit +2 to energy gain per turn"
        self.alters.append(Energy_Gain(True, 0, True, owner, 2, self))

class Tri_Charm_Amulet(Item):
    def __init__(self, owner: Unit):
        self.owner = owner
        self.name = "Tri Charm Amulet"
        self.description = "Gives unit a +1 boost to movement, vision, and eg"
        self.alters.append(Speed(True, 0, True, owner, 1, self))
        self.alters.append(Vision(True, 0, True, owner, 1, self))
        self.alters.append(Energy_Gain(True, 0, True, owner, 1, self))
