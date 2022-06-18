# The different specific Guards that can be played

from Unit import *
from random import randrange
from Summons import *

# Blood Hunter
# Guard that tracks down enemies through the forest
# Capable of walking through forest, unlike other Guards
class Blood_hunter(Guard):

    def __init__(self, location: Tile):
        self.location = location
        self.attack_range = 1
        self.movement = randrange(5,7)
        # The bloodhunter can only see what is immediately around it
        self.vision = 1
        self.energy_gain = randrange(2,4)

    # Represented on the map by B
    def get_symbol(self) -> str:
        return "B"

    def print_stats(self):
        print("Blood Hunter" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\Attack Range: " + attack_range)
        # Print Abilities
        self.print_abilities()

    # Prints out a list of the units abilities
    def print_abilities(self):
        print("\nAbilities\n"
        + "Track: Detect places where Thieves have been recently"
        + "Blood Scent: Sniff out nearby enemies\n"
        + "Blood Rite: Destroy Thieves in a 3x3 grid")

    # Blood Hunter can move through forest tiles, like a Thief
    # They still cannot see through forests
    # Override the default move function
    def move(self, map: Map, new_location: int):
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

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
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

    # Indicate tiles that Thieves have been on in the last 2 turns
    def track(self, map: Map):
        self.energy -= 3
        # TODO: Implement this, requires remembering unit locations

    # Smell enemies within range 3 and reveal them
    def blood_scent(self, map: Map):
        self.energy -= 3
        # get range 3 square
        smell_zone = grab_square(map, map.tile_list[self.location], 3)
        for tile in smell_zone:
            if (tile.occupied == True):
                # If thief is on tile, make them visible
                if (isinstance(tile.occupant, Thief)):
                    tile.occupant.visible = True

    # Area targetted effect slaying all thieves in a 3x3 grid
    def blood_rite(self, map: Map, target: Tile):
        self.energy -= 5
        # Get 3x3 zone around target tile
        kill_zone = grab_square(map, target, 1)
        # Kill everything in zone
        for tile in kill_zone:
            if (tile.occupied == True):
                tile.occupant.kill()

# Golem
# Beefy Guard thats resilient and strong
# Disable method in Unit (also works for temporary immunity alters)
class Golem(Guard):
    # Block indicates whether a disable will be blocked
    block = False
    # Overcharge state will cause the golem to autokill any thief attacked
    overcharge = False

    def __init__(self, location: Tile):
        self.location = location
        self.movement = randrange(2,4)
        self.vision = randrange(3,5)
        self.energy_gain = randrange(2,4)
        self.attack_range = 1

    # Represented on the map by G
    def get_symbol(self) -> str:
        return "G"

    def print_stats(self):
        print("Golem" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\Attack Range: " + attack_range + "\nAbilities\n")
        # Print Abilities
        self.print_abilities()

    # Prints out a list of the units abilities
    def print_abilities(self):
        print("\nAbilities\n"
        + "Charge: Dash to target tile, and disable nearby thieves\n"
        + "Smash: Destroy nearby wall, making it a field\n"
        + "Armor Up: Block the next disabling effect for 3 turns")

    # Overwrites the disable function to allow blocking to work
    def disable(self):
        if (self.block == True):
            print("Disable blocked by Golem's power armor")
            self.block = False
        else:
            self.disabled = True

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
        if (choice == "1"):
            # TODO: Implement targetting system
            self.charge(map, target)
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.smash(map, target)
        elif (choice == "3"):
            self.armor_up()
        elif (choice == "4"):
            self.double_hit()
        else:
            print("Invalid selection")
            return "invalid"

    # Charges toward a target, disabling them
    def charge(self, map: Map, target: Tile):
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
    def smash(self, map: Map, target: Tile):
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
        # Sets block to True, enabling blocking of disable
        block = True

    # SHOULD this return a variable to indicate turn is over????
    # Ends your turn.  During your next turn, all attacks will auto-kill Thieves
    def overcharge(self):
        self.energy -= 5
        # Turns overcharge on
        overcharge = True

# Techie
# Trap-laying Guard with unique utility
class Techie(Guard):

    def __init__(self, location: Tile):
        self.location = location
        self.movement = randrange(2,3)
        self.vision = randrange(3,5)
        self.energy_gain = randrange(3,5)
        self.attack_range = 2

    # Represented on the map by T
    def get_symbol(self) -> str:
        return "T"

    def print_stats(self):
        print("Techie" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\Attack Range: " + attack_range)
        # Print Abilities
        self.print_abilities()

    # Prints out a list of the units abilities
    def print_abilities(self):
        print("\nAbilities\n"
        + "Statis Trap: Drop a stasis trap, disabling thieves that come close\n"
        + "Scan: Reveal an area of the map for 1 turn\n"
        + "Hack: Reduce energy gain of all thieves for 2 turns")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
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
    def stasis_trap(self, map: Map, target: Tile):
        if ((target.type == 0) and (target.occupant == False)):
            self.energy -= 5

            #Create summon on this tiles
            target.occupant = Stasis_trap(target.id, self)
        else:
            print("Can't place trap here")

    # Scan a target area, giving temporary Vision in 5x5 grid
    def scan(self, map: Map, target: Tile):
        self.energy -= 4
        # Get 5x5 grid around target
        scan_zone = grab_square(map, target, 2)
        # TODO: add grabbed tiles to vision
        # Should visible tiles even be a set at this point?

    # Reduce vision of all enemies on the map_array
    def hack(self, thief_list: List):
        self.energy -= 3
        # Add a vision debuff alter to each thief
        for thief in thief_list:
            thief.alters.append(Vision_Alter(hack, False, 3, False, thief, 2, self))

# Sniper
# Sharpshooter good at holding down space and slaying Thieves from longe range
class Sniper(Guard):

    def __init__(self, location: Tile):
        self.location = location
        self.movement = randrange(2,4)
        self.vision = randrange(6,8)
        self.energy_gain = randrange(2,3)
        self.attack_range = 4

    # Represented on the map by G
    def get_symbol(self) -> str:
        return "N"

    def print_stats(self):
        print("Sniper" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain))
        # Print Abilities
        self.print_abilities()

    # Prints out a list of the units abilities
    def print_abilities(self):
        print("\nAbilities\n"
        + "Intuition: Intuit locatino of nearest Thief, giving a direction"\n"
        + "Take Aim: Gain increased aim until your next turn\n"
        + "Prowl: Gain level 1 stealth until your next turn")

    # Takes input from player asking which ability to be used, executes
    # appropriately in sub class
    def ability_selection(self, map: Map, choice: int):
        if (choice == "1"):
            # TODO: Implement targetting system
            self.intuition(map)
        elif (choice == "2"):
            # TODO: Implement targetting system
            self.take_aim()
        elif (choice == "3"):
            self.prowl()
        else:
            print("Invalid selection")
            return "invalid"

    # The Sniper gains an idea of where the nearest thief is, indicating
    # a direction
    def intuition(self, map: Map, thief_list: List):
        self.energy -= 3

        # Find closest thief, spiraling out from current location
        closest = None
        distance = 1
        while (closest == None):
            square = map.grab_square(self.location.id, distance)
            for tile in square:
                if (tile.occupant):
                    closest = tile.occupant

        # Add the closest thieves tile to vision
        self.visible_tiles.add(closest.location)

    # Sniper increases his attack range for this turn
    def take_aim(self):
        self.energy -= 2
        # Create an alter that increases attack_range temporarily
        # Apply it then add it to the alter list
        take_aim_buff = Alter("Take Aim", False, 1, True, self, 2, self)
        take_aim_buff.apply()
        self.alters.append(take_aim_buff)

    # Gain minor invisibility until your next turn
    def prowl(self):
        self.energy -= 3
        # Create an alter that increases stealth temporarily
        # Apply it then add it to the alter list
        prowl_buff = Speed_Alter("Prowl", False, 1, True, self, 1, self)
        prowl_buff.apply()
        self.alters.append(prowl_buff)
