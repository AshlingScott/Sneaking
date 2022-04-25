# Unit - Abstract
# Class representing Units that move on the maps
# Units can be Thief or Guard, which are opposing types

from abc import *
from random import randrange

from Map import *

class Unit(ABC):
    # Whether enemy team can see Unit
    visible = False
    # Disabled units lose their next turn
    disabled = False
    # Flying units can move on any tiles and can see over walls/forest
    flying = False
    # Stealth value 0 is fully visible, 1 is light invis, 2 is heavy invis
    stealth = 0
    # Energy is a resource used for abilities
    energy = 0
    # Set of tiles that are visible by character
    visible_tiles = set()
    # List of items held
    items = []
    # List of all alters affecting the character
    alters = []
    # List of all summons controlled by character
    summons = []
    # List of all talents allocated by characters
    talents = []
    # How many talent points are available
    talent_points = 0

    # Other stats (set by class constructors):
    # Movement: How many tiles a Unit can move in one turn
    # Vision: How far a Unit can see
    # Energy_gain: How much energy a Unit gains each turn

    @abstractmethod
    def __init__(self):
        pass

    # Get symbol returns a symbol to display on the map, representing
    # the characters location
    @abstractmethod
    def get_symbol(self):
        pass

    # Print_stats prints out a list of relevant attributes of a unit.
    @abstractmethod
    def print_stats(self):
        pass

    # Kill is how Thieves are removed from the round after being hit
    # The kill funciton might be better off simply belonging to Thief
    @abstractmethod
    def kill(self):
        pass

    # Each turn, move through lists.  Apply alters,
    # updating durations and per-turn effects
    def upkeep(self):
        # Loop through lists to tick down durations of alters and summons
        for x in range(len(self.alters)):
            if (self.alters[x].tick_down() == 0):
                self.alters.pop(x)
        for x in range(len(self.summons)):
            if (self.summons[x].tick_down() == 0):
                self.summons.pop(x)

        # Apply Alters
        for alter in self.alters:
            alter.apply()

        # Increment energy by energy_gain
        self.energy += self.energy_gain

    # Disable method sets status of the unit to disabled.  This is a function
    # to allow overwriting potential
    def disable(self):
        self.disabled = True

    # Apply effects that expire at end of a turn
    def end_turn(self):
        # Remove disabled effect
        self.disabled = False

    # Equips an item to the Unit
    def add_item(self, item):
        # Add item to players item list
        self.items.append(item)
        # Add the items alters to the players alter list
        self.alters += item.alters

    # Print out a list of items unit is holding
    def print_items(self):
        for item in self.items:
            print(item.description)

# Thief
#Sneak into the base and steal treasures to win rounds
class Thief(Unit):
    # Whether the Thief is alive
    alive = True
    # Whether Thief is holding the treasure
    has_treasure = False

    # Kills the thief
    def kill(self, map: Map):
        alive = False
        map.tile_list[self.location].occupied = False
        map.tile_list[self.location].occupant = None

    # Moves to target tile, Thieves can move on 0 or 1 type tiles
    def move(self, map: Map, new_location: Tile):
        if (new_location.type <= 1):
            # Remove from previous location
            self.location.occupant = None
            # Update to new location
            self.location = new_location
            new_location.occupant = self
            # Update visible_tiles
            self.update_vision(map)
        else:
            # If move isn't valid, return as a fail
            print("Cannot move to location")
            return True

    # Gets vision range of Unit, Thieves can see type 0 and 1 tiles
    def get_vision(self, map: Map) -> set:
        vision_tiles = set()
        # Grab a square based on Units vision
        grab_vision = map.grab_square(map, self.location, self.vision)
        # Adds only tiles of type 0 or 1 to the set
        for val in grab_vision:
            if (val.type < 2):
                vision_tiles.add(val)

        return vision_tiles

        # TODO: Add alter / item based vision to the set

# Guard
# Prevent thieves from breaking in to win rounds
class Guard(Unit):
    # List of tiles that are lighted up by character
    light_area = []

    # Guards can't die
    def kill(self):
        pass

    # Moves to target tile, Guards can only move on 0 tiles
    def move(self, map: Map, new_location: int):
        if (map.tile_list[new_location].type == 0):
            # Remove from previous location
            self.location.occupant = None
            # Update to new location
            self.location = new_location
            new_location.occupant = self
            # Update visible_tiles
            self.update_vision(map)

            vision = self.get_vision(map)
            for summon in summons:
                vision = vision.union(summon.get_vision(map))
            visible_tiles = vision

        else:
            # If move isn't valid, return as a fail
            print("Cannot move to location")
            return True

    # Gets visible tiles of Unit.  Guards can see type 0 tiles only
    def get_vision(self, map: Map) -> set:
        vision_tiles = set()
        # Grab a square based on Units vision
        grab_vision = map.grab_square(map, self.location, self.vision)
        # Adds only tiles of type 0 to the set
        for val in grab_vision:
            if (val.type == 0):
                vision_tiles.add(val)

        return vision_tiles

# Rosters are collections of Units.  A Team is a selection of Units
# from a roster for a given game/mission/map
class Roster:
    # Max number of units on a roster
    maximum = 10
    # List of units on roster
    unit_list = []

    def __init__(self):
        pass

    # Add a unit to the rester, if the roster is already full return false
    def add_unit(self, unit: Unit):
        if (len(self.unit_list) < self.maximum):
            self.unit_list.append(unit)
        else:
            print("Roster size is maximum already")
            return False

class Team:
    # Max number of units on a Team
    maximum = 3
    # List of units on Team
    unit_list = []

    def __init__(self):
        pass

    # Add a unit to the rester, if the roster is already full return false
    def add_unit(self, unit: Unit):
        if (len(self.unit_list) < self.maximum):
            self.unit_list.append(unit)
        else:
            print("Team size is maximum already")
            return False

# The recruiting shop where you can purchase new units
# Currently offers 3 random units, with different prices
class Recruit_Board():
    # List of recruits in the shop
    recruits = []
    # prices of recruits
    prices = []

    # Create 3 random characters and add to board
    def __init__(self):
        for x in range(3):
            z = randrange(0,5)
                self.recruits.append(random_unit())
                # Set price in corresponding list
                self.prices.append(rangerange(0,5))

    # Create a random unit.  Used on initialization and when a purchase is made
    def random_unit() -> Unit:
        z = randrange(0,5)
        if (z == 0):
            unit = Druid(None)
        elif (z == 1):
            unit = Sprinter(None)
        elif (z == 2):
            unit = Shadow(None)
        elif (z == 3):
            unit = Blood_hunter(None)
        elif (z == 4):
            unit = Golem(None)
        else:
            unit = Techie(None)

        return unit

    # Select a unit from the board and add it to the roster, then replace
    def select_unit(roster: Roster, choice: int):
        # Tries to add a unit, only on succeeding will it make a new one
        if (roster.add_unit(self.recruits[choice-1])):
            self.recruits[choice-1] = random_unit()
            prices[choice-1] = randrange(0,5)
        else:
            print("Roster is full")

    # Prints out the list of current units on the recruit board
    def print_board():
        for x in range(3):
            print{"\n"}
            recruits.print_stats()
            print{"\n"}
            print(self.prices[x])
