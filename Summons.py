# Summons, created on the map to be separate units
# Has similarities with Character class, but functionally seperate

from Unit import *

class Summons:
    visible = False
    disabled = False
    flying = False
    # Stealth value 0 is fully visible, 1 is light invis, 2 is heavy invis
    stealth = 0
    energy = 0
    # List of tiles that are visible by character
    visible_tiles = []
    # List of all alters affecting the character
    alter = []

    def __init__(self, controller, duration, permanent, x, y, m, v, e_g):
        self.controller = controller
        self.duration = duration
        self.permanent = permanent
        self.location = (x, y)
        self.movement = m
        self.vision = v
        self.energy_gain = e_g

    # Ticks down the duration of temporary summons, returns duration
    def tick_down(self):
        if (self.permanent == False):
            self.duration -= 1
        return duration
