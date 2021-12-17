# The various summons that can be summoned
from Unit import *

#  Summoned by the Hunter Guard, wolves are fast and (???)
class Wolf(Summon):

    # Represented on the map with W
    def get_symbol(self):
        return "W"

    def print_stats(self):
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nDuration Remaining: " + str(self.duration))
