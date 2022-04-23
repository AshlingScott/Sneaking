# Summon, created on the map to be separate units
# Has similarities with Character class, but functionally seperate

from Unit import *

class Summon(Unit):

    # Moves to target tile, by default Summons can only move on 0 tiles
    def move(self, map: Map, new_location: Tile):
        if (map.tile_list[new_location.id].type == 0):
            # Remove from previous location
            map.tile_list[self.location.id].occupant = None
            # Update to new location
            self.location = new_location
            map.tile_list[new_location.id].occupant = self
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
    def get_vision(self, map: Map) -> set:
        vision_tiles = set()
        # Grab a square based on Units vision
        grab_vision = map.grab_square(map, self.location, self.vision)
        # Adds only tiles of type 0 to the set
        for val in grab_vision:
            if (val.type == 0):
                vision_tiles.add(val)

        return vision_tiles

    # Ticks down the duration of temporary summons, returns duration
    def tick_down(self) -> int:
        if (self.permanent == False):
            self.duration -= 1
        return duration

#  Summoned by the Hunter Guard, wolves are fast and (???)
class Wolf(Summon):

    permanent = False

    # Wolves have 6 movement, 4 vision, and no energy or energy gain
    # Duration of 3 turns
    def __init__(self, location: Tile, own: Unit):
        self.location = location
        self.owner = own

        self.movement = 6
        self.vision = 4
        self.energy_gain = 0
        self.duration = 3

    # Represented on the map with W
    def get_symbol(self) -> str:
        return "W"

    def print_stats(self):
        print("Wolf" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nDuration Remaining: " + str(self.duration))

#  Stasis traps are permanent summons that wait for a thief to walk over them
#  and destroy themselves to disable the triggerer
class Stasis_trap(Summon):

    permanent = True

    # Stasis has no movement and no vision
    def __init__(self, location: Tile, own: Unit):
        self.location = location
        self.owner = own

        self.movement = 0
        self.vision = 0
        self.energy_gain = 0
        self.duration = 0

    # Represented on the map with @
    def get_symbol(self) -> str:
        return "@"

    def print_stats(self):
        print("Stasis Trap" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nPermanent Duration")

    # Detonates the trap when a Thief steps on it, disabling the thief
    def detonate(self, thief: Thief, owner: Unit, map: Map):
        thief.disabled = True
        location.occupant = None

        #TODO: Implement logic for stepping on mines
        # Probably part of the move function (When checking for collision,
        # if its a mine let them walk there and detonate)
