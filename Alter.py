# Alters are changes to the properties of a character.  They can
# be either permanent or temporary, and be either positive or negative

from abc import *
from Unit import *

class Alter(ABC):

    @abstractmethod
    def __init__(self):
        pass

# Integer Alters provide a flat integer buff to an attribute
class Integer_Alter(Alter):
    # Positive is whether the alter is beneficial or harmful
    # Magnitude is an integer value associated with the alter strength
    # Source is the source of the alter, usually either a Unit or Item
    def __init__(self, name: str, permanent: bool, duration: int, positive: bool,
            own: Unit, mag: int, source):
        self.name = name
        self.permanent = permanent
        self.duration = duration
        self.positive = positive
        self.owner = own
        self.magnitude = mag
        self.source = source

    # Apply applies effects to a character during the upkeep step
    @abstractmethod
    def apply(self):
        pass

    # Ticks down the duration of each alter, returns duration
    def tick_down(self) -> int:
        if (self.permanent == False):
            self.duration -= 1
        else:
            self.duration = -1
        return self.duration

# Speed alter, found on Boots of Speed or speed boosts
class Speed_Alter(Integer_Alter):

    def apply(self):
        self.owner.movement += self.magnitude
    def remove(self):
        self.owner.movement -= self.magnitude

# Vision alter, found on spyglass or vision boosts
class Vision_Alter(Integer_Alter):

    def apply(self):
        self.owner.vision += self.magnitude

    def remove(self):
        self.owner.vision -= self.magnitude

# Max Energy alter, found on Power Well
class Energy_Alter(Integer_Alter):

    def apply(self):
        self.owner.energy += self.magnitude

    def remove(self):
        self.owner.energy -= self.magnitude

# Energy gain alter, found on Energy Charm
class Energy_Gain_Alter(Integer_Alter):

    def apply(self):
        self.owner.energy_gain += self.magnitude

    def remove(self):
        self.owner.energy_gain -= self.magnitude

# Range increase Alters
class Attack_Range_Alter(Integer_Alter):

    def apply(self):
        self.owner.attack_range += self.magnitude

    def remove(self):
        self.owner.energy_gain -= self.magnitude

class Stealth_Buff(Integer_Alter):

    def apply(self):
        self.owner.stealth += self.magnitude

    def remove(self):
        self.owner.stealth -= self.magnitude

# Creates a temporary field of vision (or blocks one?)
class Tile_Vision(Alter):

    def __init__(self, name: str, permanent: bool, duration: int,
            own: Unit, vis: set, source):
        self.name = name
        self.permanent = permanent
        self.duration = duration
        self.owner = own
        self.visible_set = vis
        self.source = source

    def apply(self):
        self.owner.visible_tiles.add(visible_set)

    def remove(self):
        #TODO: reset vision to normal
