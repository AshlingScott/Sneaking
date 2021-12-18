# The different specific Thieves that can be played

from Unit import *

# Druid
# Flexible Thief that can change their form to suit their purpose
class Druid(Thief):
    # Druids base stats are:
    # 4 Movement
    # 5 Vision
    # 3 Energy Gain
    def __init__(self, location):
        self.location = location
        self.movement = 4
        self.vision = 5
        self.energy_gain = 3
        # Form represents what the druid is shapeshifted into
        # 0 is Human (default), 1 is hawk, 2 is squirrel
        self.form = 0

    # Represented on the map with D
    def get_symbol(self):
        return "D"

    def print_stats(self):
        if (self.form == 0):
            form = "Human"
        if (self.form == 1):
            form = "Hawk"
        if (self.form == 2):
            form = "Squirrel"
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nCurrent Form: " + form + "\nAbilities\n"
        + "Entangle: Trap an enemy with roots\n"
        + "Hawk Form: Turn into a hawk, gain flying and extra vision\n"
        + "Squirrel Form: Turn into a squirrel, gain movement and stealth\n"
        + "Overgrowth: Grow a patch of trees in an area\n")

    # Wraps the target in roots, disabling for 1 turn
    def entangle(self, target):
        self.energy -= 3
        target.disabled = True
        # TODO: Make it an alter with duration

    # Transform into a hawk, gaining vision and flying
    def hawk_form(self):
        # If in hawk form alread, swap to human
        if (self.form == 1):
            self.form = 0
            self.vision -= 3
            self.flying = False
        # Otherwise switch to hawk
        else:
            self.form = 1
            self.energy -= 3
            self.vision += 3
            self.flying = True

    # Transform into a Squirrel, gaining movement speed and stealth
    def squirrel_form(self):
        # If in squirrel form alread, swap to human
        if (self.form == 2):
            self.form = 0
            self.movement -= 2
            self.stealth -=1
        # Otherwise switch to squirrel
        else:
            self.form = 2
            self.energy -= 3
            self.movement += 2
            self.stealth += 1

    # Create a patch of trees in a 3x3 grid
    def overgrowth(self, map, target):
        self.energy -= 5
        # Get 3x3 of tiles around target tile
        tiles = grab_square(map, target, 1)
        for val in tiles:
            # Transform to trees
            if (val.type <= 1):
                val.type = 1

# Sprinter
# Agile Thief able to outrun enemies
class Sprinter(Thief):
    # Sprinters base stats are:
    # 6 Movement
    # 4 Vision
    # 2 Energy Gain
    def __init__(self, location):
        self.location = location
        self.movement = 6
        self.vision = 4
        self.energy_gain = 2

    # Represented on the map with S
    def get_symbol(self):
        return "S"

    def print_stats(self):
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Sprint: Run faster for 2 turns\n"
        + "Throw: Throw an item or a treasure to another Thief\n"
        + "Vault: Leap to target tile, can jump onto walls (can walk off later)")

    # Run very fast for one round
    def sprint(self):
        self.energy -= 3
        self.movement += 3
        # TODO: Make it an alter with duration

    # Throws an item to another Thief
    def throw(self, target):
        if self.has_treasure:
            self.energy -= 3
            self.has_treasure = False
            target.has_treasure = True
        else:
            print("Nothing to throw!")
        # TODO: Implement throwing other items besides treasure

    # Leaps to a tile, can target walls (you can walk off of walls as normal)
    # Range of 2
    def vault(self, map, target):
        # Get list of tiles within range of 2
        viable_tiles = map.grab_square(map, map.tile_list[self.location], 2)
        # Check if target tile is within that list
        if target in viable_tiles:
            self.energy -= 4
            self.location = target
        else:
            print("Location invalid, out of range")

# Shadow
# Slippery Thief that hides in the darkness
class Shadow(Thief):
    # Shadows base stats are:
    # 3 Movement
    # 5 Vision
    # 3 Energy Gain
    def __init__(self, location):
        self.location = location
        self.movement = 3
        self.vision = 5
        self.energy_gain = 3
        # Shadows have a default stealth level of 1 instead of 0
        self.stealth = 1

    # Represented on the map with H
    def get_symbol(self):
        return "H"

    def print_stats(self):
        print("Shadow" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Shadow Dance: Gain increased stealth for 2 turns\n"
        + "Dark Warp: Teleport to target tile\n"
        + "Blind: Reduce the vision of a Guard by 2 for 2 turns")

    # Becomes covered in shadows, gaining increased stealth
    def shadow_dance(self):
        self.energy -= 2
        self.stealth = 2
        # TODO: Make it an alter with duration

    # Warps to target location
    def dark_warp(self, target):
        self.energy -= 4
        self.location = target

    # Covers a guard in shadows, reducing their vision range
    def blind(self, map, target):
        self.energy -= 4
        target.vision -= 2
        # Immediately updates visiion of target guard
        target.update_vision(map)
        # TODO: Make it an alter with duration
