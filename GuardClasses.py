# The different specific Guards that can be played

from Character import *

class Blood_hunter(Guard):
    # Smell nearby enemies and reveal them
    def blood_scent(self):
        self.energy -= 3
        # Todo: find enemies in an area and make them visible

    # Area targetted effect slaying all thieves in a 3x3 grid
    def blood_rite(self, target):
        self.energy -= 5
        # Todo: if thieves are in the area, kill them

class Golem(Guard):
    # Charges toward a target, disabling them
    def charge(self, target):
        self.energy -= 5
        self.location = target

        # Todo: find nearby Thieves and disable them

    # Smash a target wall, turning it into grass
    def smash(self, target):
        if (target.type == 2):
            self.energy -= 3
            target.type = 0
        else:
            pass

class Techie(Guard):
    # Drop a stasis trap on a tile, disables thieves who step too close
    def stasis_trap(self, target):
        if (target.type == 0):
            self.energy -= 5
            #Todo: create summon on this tiles
        else:
            pass

    # Scan a target area, giving temporary Vision
    def scan(self, map, target):
        self.energy -= 4
        self.visible_tiles.append(target)
        #Todo: add surrounding tiles to visible_tiles as well

    # Reduce vision of all enemies on the map_array
    def hack(self, thief_list):
        self.energy -= 3
        for x in range(len(thief_list)):
            thief_list[x].vision -= 2
