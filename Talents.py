# Talents are the bonuses characters earn from levelling up
# Talents can be active abilities or passive buffs

from abc import *

class Talent(ABC):

    def __init__(self, id: int, active: Boolean, tier: int,
            connection: list, effects: list):
        self.id = id
        self.active = active
        self.tier = tier
        self.connection = connection
        self.effect = effects

class TalentTree:

    def __init__(self):
        pass
        # Load talent tree

        # Create Talents

        # Links talents together
