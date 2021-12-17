# Unit - Abstract
# Class representing Units that move on the maps
# Units can be Thief or Guard, which are opposing types

from abc import *
from Map import *

class Unit(ABC):
    # Whether enemy team can see Unit
    visible = False
    # Disabled units lose their next turn
    disabled = False
    # Flying units can move on any tiles and can see over walls/forest
    flying = False
    # Whether Unit is holding the treasure
    has_treasure = False
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

    # Location: ID of this Units tile on the grid
    # Movement: How many tiles a Unit can move in one turn
    # Vision: How far a Unit can see
    # Energy_gain: How much energy a Unit gains each turn
    def __init__(self, location, movement, vision, energy_gain):
        self.location = location
        self.movement = movement
        self.vision = vision
        self.energy_gain = energy_gain

    # Abstract methods.  Get symbol returns a vaue to display on the printout
    # map.  Print_stats prints out a list of relevant attributes of a unit.
    # Kill is how Thieves are removed from the round after being hit
    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def print_stats(self):
        pass

    # The kill funciton might be better off simply belonging to Thief
    @abstractmethod
    def kill(self):
        pass

    # Each turn, move through lists.  Apply alters,
    # updating durations and per-turn effects
    def upkeep(self):

        print(self.alters)
        # Loop through lists to tick down durations
        for x in range(len(self.alters)):
            if (self.alters[x].tick_down() == 0):
                self.alters.pop(x)
        for x in range(len(self.summons)):
            if (self.summons[x].tick_down() == 0):
                self.summons.pop(x)

        print(self.alters)

        # Apply Alters
        for alter in self.alters:
            print("applying")
            alter.apply()

        # Increment energy by energy_gain
        self.energy += self.energy_gain

    # Print out a list of items character is holding
    def print_items(self):
        for x in range(len(self.items)):
            print(self.items[x].description)

# Thief - Abstract
#Sneak into the base and steal treasures to win rounds
class Thief(Unit):
    # Whether the Thief is alive
    alive = True

    # Kills the thief
    def kill(self, map):
        alive = False
        map.tile_list[self.location].occupied = False
        map.tile_list[self.location].occupant = None

    # Moves to target tile, Thieves can move on 0 or 1 type tiles
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

    # Gets vision range of Unit, Thieves can see type 0 and 1 tiles
    def update_vision(self, map):
        vision_tiles = set()
        # Grab a square based on Units vision
        grab_vision = map.grab_square(map, map.tile_list[self.location], self.vision)
        # Adds only tiles of type 1 or 0 to the set
        for tile in grab_vision:
            if (tile.type <= 1):
                vision_tiles.add(tile)

        visible_tiles = vision_tiles

        # TODO: Add alter / item based vision to the set

# Guard - Abstract
# Prevent thieves from breaking in to win rounds
class Guard(Unit):
    # List of tiles that are lighted up by character
    light_area = []

    # Guards can't die
    def kill(self):
        pass

    # Moves to target tile, Guards can only move on 0 tiles
    def move(self, map, new_location):
        if (map.tile_list[new_location].type == 0):
            # Remove from previous location
            map.tile_list[self.location].occupant = None
            map.tile_list[self.location].occupied = False
            # Update to new location
            self.location = new_location
            map.tile_list[new_location].occupied = True
            map.tile_list[new_location].occupant = self
            # Update visible_tiles
            vision = self.get_vision(map)
            for summon in summons:
                vision = vision.union(summon.get_vision(map))
            visible_tiles = vision

        else:
            # If move isn't valid, return as a fail
            print("Cannot move to location")
            return True

    # Gets visible tiles of Unit.  Guards can see type 0 tiles only
    def get_vision(self, map):
        vision_tiles = set()
        # Grab a square based on Units vision
        grab_vision = map.grab_square(map, map.tile_list[self.location], self.vision)
        # Adds only tiles of type 0 to the set
        for val in grab_vision:
            if (val.type == 0):
                vision_tiles.add(val)

        return vision_tiles

# Summon, created on the map to be separate units
# Has similarities with Character class, but functionally seperate
class Summon(Unit):
    permanent = False
    duration = 0

    # Calls the unit constructor, then adds duration and ownership attributes
    def __init__(self, location, movement, vision, energy_gain, dur, perm, own):
        super().__init__(location, movement, vision, energy_gain)
        self.owner = own
        if (perm):
            self.permanent = True
        else:
            self.duration = dur

    # Kills the Summon
    # Not sure if required to implement at the moment
    def kill(self, map):
        pass

    # Moves to target tile, default Summons can only move on 0 tiles
    def move(self, map, new_location):
        if (map.tile_list[new_location].type == 0):
            # Remove from previous location
            map.tile_list[self.location].occupant = None
            map.tile_list[self.location].occupied = False
            # Update to new location
            self.location = new_location
            map.tile_list[new_location].occupied = True
            map.tile_list[new_location].occupant = self
            # Update visible_tiles
            vision = owner.get_vision(map)
            for summon in owner.summons:
                vision = vision.union(summon.get_vision(map))
            owner.visible_tiles = vision

        else:
            # If move isn't valid, return as a fail
            print("Cannot move to location")
            return True

    # Gets visible tiles of the Summon.  Summons by default can only see 0
    def get_vision(self, map):
        vision_tiles = set()
        # Grab a square based on Units vision
        grab_vision = map.grab_square(map, map.tile_list[self.location], self.vision)
        # Adds only tiles of type 0 to the set
        for val in grab_vision:
            if (val.type == 0):
                vision_tiles.add(val)

        return vision_tiles

    # Ticks down the duration of temporary summons, returns duration
    def tick_down(self):
        if (self.permanent == False):
            self.duration -= 1
        return duration
