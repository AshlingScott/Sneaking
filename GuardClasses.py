# The different specific Guards that can be played

from Unit import *

# Blood Hunter
# Guard that tracks down enemies through the forest
# Capable of walking through forest, unlike other Guards
class Blood_hunter(Guard):
    # Blood Hunter base stats are:
    # 6 Movement
    # 2 Vision
    # 3 Energy Gain
    def __init__(self, location):
        self.location = location
        self.movement = 6
        self.vision = 2
        self.energy_gain = 3

    # Represented on the map by B
    def get_symbol(self):
        return "B"

    def print_stats(self):
        print("Blood Hunter" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Track: Detect places where Thieves have been recently"
        + "Blood Scent: Sniff out nearby enemies\n"
        + "Blood Rite: Destroy Thieves in a 3x3 grid")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map, choice):
        if (choice == "1"):
            self.track()
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.blood_scent(map)
        elif (choice == "3"):
            # TODO: Implement targetting system
            self.blood_rite(map, target)
        else:
            print("Invalid selection")
            return "invalid"

    # Blood Hunter can move through forest tiles, like a Thief
    # They still cannot see through them
    def move(self, map, new_location):
        if (map.tile_list[new_location].type <= 1):
            # Remove from previous location
            map.tile_list[self.location].occupant = None
            map.tile_list[self.location].occupied = False
            # Update to new location
            self.location = new_location
            map.tile_list[new_location].occupied = True
            map.tile_list[new_location].occupant = self
            # Update visible_tiles
            self.update_vision(map)
        else:
            # If move isn't valid, return as a fail
            print("Cannot move to location")
            return True

    # Indicate tiles that Thieves have been on in the last 2 turns
    def track(self, map):
        self.energy -= 3
        # TODO: Implement this, requires remembering unit locations

    # Smell enemies within range 3 and reveal them
    def blood_scent(self, map):
        self.energy -= 3
        # get range 3 square
        smell_zone = grab_square(map, map.tile_list[self.location], 3)
        for tile in smell_zone:
            if (tile.occupied == True):
                # If thief is on tile, make them visible
                if (isinstance(tile.occupant, Thief)):
                    tile.occupant.visible = True

    # Area targetted effect slaying all thieves in a 3x3 grid
    def blood_rite(self, map, target):
        self.energy -= 5
        # Get 3x3 zone around target tile
        kill_zone = grab_square(map, target, 1)
        # Kill everything in zone
        for tile in kill_zone:
            if (tile.occupied == True):
                tile.occupant.kill()

# Golem
# Beefy Guard thats resilient and strong
# TODO: Implement immunity to disables.  This might require an abstract
# Disable method in Unit (also works for temporary immunity alters)
class Golem(Guard):
    # Golem base stats are:
    # 3 Movement
    # 5 Vision
    # 2 Energy Gain
    def __init__(self, location):
        self.location = location
        self.movement = 3
        self.vision = 5
        self.energy_gain = 2

    # Represented on the map by G
    def get_symbol(self):
        return "G"

    def print_stats(self):
        print("Golem" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Charge: Dash to target tile, and disable nearby thieves\n"
        + "Smash: Destroy nearby wall, making it a field\n"
        + "Armor Up: Block the next disabling effect for 3 turns")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map, choice):
        if (choice == "1"):
            # TODO: Implement targetting system
            self.charge(map, target)
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.smash(map, target)
        elif (choice == "3"):
            self.armor_up()
        else:
            print("Invalid selection")
            return "invalid"

    # Charges toward a target, disabling them
    def charge(self, map, target):
        failed = move(map, target)
        # If move failed, do nothing
        if failed:
            print("Cannot charge to that tile")
        # On successful move, disable nearby Thieves
        else:
            self.energy -= 3
            # Get 3x3 zone around new location
            stun_zone = grab_square(map, map.tile_list[self.location], 1)
            for tile in stun_zone:
                if (tile.occupied == True):
                    # Disable thieves in stun zone
                    if (isinstance(tile.occupant, Thief)):
                        tile.occupant.disabled = True
            # TODO: Add disable as a duration alter

    # Smash a target wall, turning it into grass
    def smash(self, map, target):
        if (target.type == 2):
            # Check melee range
            melee_zone = grab_square(map, map.tile_list[self.location], 1)
            if target in melee_zone:
                # Turn wall into field
                self.energy -= 3
                target.type = 0
            else:
                print("Target is out of range (range of 1)")
        else:
            print("Targetted tile is not a wall")

    # Block the next disabling effect, last 3 returns
    def armor_up(self):
        self.energy -= 3
        # TODO: Add a duration alter for block effect

# Techie
# Trap-laying Guard with unique utility
class Techie(Guard):
    # Techie base stats are:
    # 3 Movement
    # 5 Vision
    # 3 Energy Gain
    def __init__(self, location):
        self.location = location
        self.movement = 3
        self.vision = 5
        self.energy_gain = 3

    # Represented on the map by T
    def get_symbol(self):
        return "T"

    def print_stats(self):
        print("Techie" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nAbilities\n"
        + "Statis Trap: Drop a stasis trap, disabling thieves that come close\n"
        + "Scan: Reveal an area of the map for 1 turn\n"
        + "Hack: Reduce energy gain of all thieves for 2 turns")\

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map, choice):
        if (choice == "1"):
            # TODO: Implement targetting system
            self.stasis_trap(map, target)
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.scan(map, target)
        elif (choice == "3"):
            # TODO: Needs to pass thieves list?  Kind of weird
            self.hack()
        else:
            print("Invalid selection")
            return "invalid"

    # Drop a stasis trap on a field tile, disables thieves who step within 1 range
    def stasis_trap(self, map, target):
        if (target.type == 0):
            self.energy -= 5
            #TODO: Create summon on this tiles
        else:
            print("Can't place trap here")

    # Scan a target area, giving temporary Vision in 5x5 grid
    def scan(self, map, target):
        self.energy -= 4
        # Get 5x5 grid around target
        scan_zone = grab_square(map, target, 2)
        # TODO: add grabbed tiles to vision
        # Should visible tiles even be a set at this point?

    # Reduce vision of all enemies on the map_array
    def hack(self, thief_list):
        self.energy -= 3
        for thief in thief_list:
            thief.energy_gain -= 2
        # TODO: Apply a duration alter to effect
