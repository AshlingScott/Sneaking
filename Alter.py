# Alters are changes to the properties of a character.  They can
# be either permanent or temporary, and be either positive or negative

from abc import *

class Alter(ABC):
    def __init__(self, permanent, duration, positive, own, mag):
        self.permanent = permanent
        self.duration = duration
        self.positive = positive
        self.owner = own
        self.magnitude = mag

    # Apply applies effects to a character during the upkeep step
    @abstractmethod
    def apply(self):
        pass

    # Ticks down the duration of each alter, returns duration
    def tick_down(self):
        if (self.permanent == False):
            self.duration -= 1
        else:
            self.duration = -1
        return self.duration

# Speed alter, found on Boots of Speed or speed boosts
class Speed(Alter):

    def apply(self):
        self.owner.movement += self.magnitude

# Vision alter, found on spyglass or vision boosts
class Vision(Alter):

    def apply(self):
        self.owner.vision += self.magnitude

class Energy(Alter):

    # Applies the effect to the owning unit
    def apply(self):
        self.owner.energy_gain += self.magnitude
