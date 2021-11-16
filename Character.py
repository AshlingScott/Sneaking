#Character class.  Characters can be either Thieves, or Guards
class Character:
    visible = False
    disabled = False
    flying = False
    has_treasure = False
    # Stealth value 0 is fully visible, 1 is light invis, 2 is heavy invis
    stealth = 0
    energy = 0
    # List of tiles that are visible by character
    visible_tiles = []
    # List of items held
    items = []
    # List of all alters affecting the character
    alter = []
    # List of all summons controlled by character
    summons = []

    # Universal Character Attributes
    # Location: x,y coordinates of this Characters position on the grid
    # Movement: How many tiles a Character can move in one turning
    # Vision: How far a Character can see
    # Energy_gain: How much energy a Character gains each turn
    def __init__(self, x, y, m, v, e_g):
        self.location = (x, y)
        self.movement = m
        self.vision = v
        self.energy_gain = e_g

    # Each turn, move through lists updating durations and per-turn effects
    def upkeep(self):
        # Increment energy by energy_gain
        self.energy += self.energy_gain
        # Loop through lists to tick down durations
        for x in range(len(self.alter)):
            if (self.alter[x].tick_down() == 0):
                self.alter.pop(x)
        for x in range(len(self.summons)):
            if (self.summons[x].tick_down() == 0):
                self.summons.pop(x))

    # Print out a list of items character is holding
    def print_items(self):
        for x in range(len(self.items)):
            print(self.items[x].description)

# Thief characters:  Sneak into the base and steal treasures to win rounds
class Thief(Character):
    dead = False

    # Moves to target tile, Thieves can move on 0 or 1 type tiles
    def move(self, map, x, y):
        if(map.tile_list[(y*10 + x)].type <= 1):
            self.location = (x, y)
        else:
            print("Cannot move to location")

# Guard characters: Prevent thieves from breaking in to win rounds
class Guard(Character):
    # List of tiles that are lighted up by character
    light_area = []

    # Moves to target tile, Guards can only move on 0 type tiles
    def move(self, map, x, y):
        if(map.tile_list[(y*10 + x)].type == 0):
            self.location = (x, y)
        else:
            print("Cannot move to location")
