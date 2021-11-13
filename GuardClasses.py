# The different specific Guards that can be played

from Character import Character
from Character import Guard

class Blood_hunter(Guard):

    # Smell nearby enemies and reveal them
    def Blood_scent(self):
        self.energy -= 3
        # Todo: find enemies in an area and make them visible

    # Area targetted effect slaying all thieves in a 3x3 grid
    def Blood_rite(self, target):
        self.energy -= 5
        # Todo: if thieves are in the area, kill them

class Golem(Guard):

    # Charges toward a target, disabling them
    def Charge(self, target):
        self.energy -= 5
        self.location = target

        # Todo: find nearby Thieves and disable them

    # Smash a target wall, turning it into grass
    def Smash(self, target):
        if (target.type = 2):
            self.energy -= 3
            target.type = 0
        else
            pass
