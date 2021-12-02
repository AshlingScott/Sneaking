# The different specific Thieves that can be played

from Unit import *

class Druid(Thief):
    # Form represents which form the Druid is in
    # 0 = base, 1 = hawk, 2 = squirrel
    form = 0

    # Represented on the map with D
    def get_symbol(self):
        return "D"

    def print_stats(self):
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nCurrent Form: ")
        if (self.form == 0):
            print("Human")
        if (self.form == 1):
            print("Hawk")
        if (self.form == 2):
            print("Squirrel")

    def kill(self):
        alive = False

    # Wraps the target in roots, disabling for 1 turn
    def entangle(self, target):
        self.energy -= 3
        target.disabled = True

    # Transform into a hawk, gaining vision and movement and flying
    def hawk_form(self):
        self.energy -= 3
        self.movement += 2
        self.vision += 3

        self.form = 1
        self.flying = True

    # Transform into a Squirrel, gaining movement speed
    def squirrel_form(self):
        self.energy -= 2
        self.movement += 4

        self.form = 2
        self.stealth = 1

    # Create a patch of trees in a 3x3 grid
    def overgrowth(self, target):
        self.energy -= 5

        target.type = 1

class Sprinter(Thief):
    # Represented on the map with S
    def get_symbol(self):
        return "S"

    def print_stats(self):
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain))

    def kill(self):
        alive = False

    # Run very fast for one round
    def sprint(self):
        self.energy -= 3
        self.movement += 3

    # Throws an item to another Thief
    def throw(self, target):
        if self.has_treasure:
            self.energy -= 3
            self.has_treasure = False
            target.has_treasure = True
        else:
            pass

    # Leaps to the top of a nearby wall
    def vault(self, target):
        if (target.type == 2):
            self.energy -= 4
            self.location = target
        else:
            pass

class Shadow(Thief):
    # Represented on the map with H
    def get_symbol(self):
        return "H"

    def print_stats(self):
        print("Shadow" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain))

    def kill(self):
        alive = False

    # Becomes covered in shadows, gaining increased stealth
    def shadow_dance(self):
        self.energy -= 2
        self.stealth = 2

    # Warps to target location
    def dark_warp(self, target):
        self.energy -= 4
        self.location = target
