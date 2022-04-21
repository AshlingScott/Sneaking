# The different specific Thieves that can be played

from Unit import *
from random import randrange

# Druid
# Flexible Thief that can change their form to suit their purpose
class Druid(Thief):
    # Druids have forms represented by numbers
    form = 0

    def __init__(self, location: int):
        self.location = location
        self.movement = randrange(3,6)
        self.vision = randrange(3,6)
        self.energy_gain = randrange(3,6)

    # Represented on the map with D
    def get_symbol(self) -> str:
        return "D"

    # Prints out stats of unit
    def print_stats(self):
        if (self.form == 0):
            form = "Human"
        if (self.form == 1):
            form = "Hawk"
        if (self.form == 2):
            form = "Squirrel"
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nCurrent Form: " + form)
        # Print abilities after attributes
        self.print_abilities()

    # Prints out a list of the units abilities
    def print_abilities(self):
        print("Abilities\n"
        + "1 - Entangle: Trap an enemy with roots\n"
        + "2 - Hawk Form: Turn into a hawk, gain flying and extra vision\n"
        + "3 - Squirrel Form: Turn into a squirrel, gain movement and stealth\n"
        + "4 - Overgrowth: Grow a patch of trees in an area\n")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
        if (choice == "1"):
            # TODO: Implement targetting system
            self.entangle(target)
        elif (choice == "2"):
            self.hawk_form()
        elif (choice == "3"):
            self.squirrel_form()
        elif (choice == "4"):
            #TODO: Implement targeting system
            self.overgrowth()
        else:
            print("Invalid selection")
            return "invalid"

    # Wraps the target in roots, disabling for 1 turn
    def entangle(self, target: Tile):
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
    def overgrowth(self, map: Map, target: Tile):
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

    def __init__(self, location: int):
        self.location = location
        self.movement = randrange(3,6)
        self.vision = randrange(3,6)
        self.energy_gain = randrange(3,6)

    # Represented on the map with S
    def get_symbol(self) -> str:
        return "S"

    def print_stats(self):
        print("Druid" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Sprint: Run faster for 2 turns\n"
        + "Throw: Throw an item or a treasure to another Thief\n"
        + "Vault: Leap to target tile, can jump onto walls (can walk off later)")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
        if (choice == "1"):
            self.sprint()
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.throw(target)
        elif (choice == "3"):
            # TODO: Implement targetting system
            self.vault(target)
        else:
            print("Invalid selection")
            return "invalid"

    # Run very fast for one round
    def sprint(self):
        self.energy -= 3
        self.movement += 3
        # TODO: Make it an alter with duration

    # Throws an item to another Thief
    def throw(self, target: Thief):
        if self.has_treasure:
            self.energy -= 3
            self.has_treasure = False
            target.has_treasure = True
        else:
            print("Nothing to throw!")
        # TODO: Implement throwing other items besides treasure

    # Leaps to a tile, can target walls (you can walk off of walls as normal)
    # Range of 2
    def vault(self, map: Map, target: Tile):
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
    # Shadows have a default stealth level of 1 instead of 0
    stealth = 1

    def __init__(self, location: int):
        self.location = location
        self.movement = randrange(3,6)
        self.vision = randrange(3,6)
        self.energy_gain = randrange(3,6)

    # Represented on the map with H
    def get_symbol(self) -> str:
        return "H"

    def print_stats(self):
        print("Shadow" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Shadow Dance: Gain increased stealth for 2 turns\n"
        + "Dark Warp: Teleport to target tile\n"
        + "Blind: Reduce the vision of a Guard by 2 for 2 turns")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
        if (choice == "1"):
            self.shadow_dance()
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.dark_warp(target)
        elif (choice == "3"):
            # TODO: Implement targetting system
            self.blind(map, target)
        else:
            print("Invalid selection")
            return "invalid"

    # Becomes covered in shadows, gaining increased stealth
    def shadow_dance(self):
        self.energy -= 2
        self.stealth = 2
        # TODO: Make it an alter with duration

    # Warps to target location
    def dark_warp(self, target: Tile):
        self.energy -= 4
        self.location = target

    # Covers a guard in shadows, reducing their vision range
    def blind(self, map, target: Guard):
        self.energy -= 4
        target.vision -= 2
        # Immediately updates visiion of target guard
        target.update_vision(map)
        # TODO: Make it an alter with duration
