# Summon, created on the map to be separate units
# Has similarities with Character class, but functionally seperate

from Unit import *

class Summon(Unit):
    # Kills the Summon
    # Not sure if required to implement at the moment
    def kill(self, map):
        pass

    # Moves to target tile, by default Summons can only move on 0 tiles
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


#  Summoned by the Hunter Guard, wolves are fast and (???)
class Wolf(Summon):
    permanent = False

    # Wolves have 6 movement, 4 vision, and no energy or energy gain
    # Duration of 3 turns
    def __init__(self, location, own):
        self.location = location
        self.owner = own

        self.movement = 6
        self.vision = 4
        self.energy_gain = 0
        self.duration = 3

    # Represented on the map with W
    def get_symbol(self):
        return "W"

    def print_stats(self):
        print("Wolf" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nEnergy: " + str(self.energy) + "\nEnergy Gain: "
        + str(self.energy_gain) + "\nDuration Remaining: " + str(self.duration))

#  Stasis traps are permanent summons that wait for a thief to walk over them
#  and destroy themselves to disable the triggerer
class Stasis(Summon):
    permanent = True

    # Stasis has no movement and no vision
    def __init__(self, location, own):
        self.location = location
        self.owner = own

        self.movement = 0
        self.vision = 0
        self.energy_gain = 0
        self.duration = 0

    # Represented on the map with @
    def get_symbol(self):
        return "@"

    def print_stats(self):
        print("Stasis Trap" + "\nMovement: " + str(self.movement) + "\nVision: "
        + str(self.vision) + "\nPermanent Duration")

    # Detonates the trap when a Thief steps on it, disabling the thief
    def detonate(self, thief, owner, map):
        thief.disabled = True
        #TODO: Implement logic for stepping on mines
        # Probably part of the move function (When checking for collision,
        # if its a mine let them walk there and detonate)
