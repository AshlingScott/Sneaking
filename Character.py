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

    # Moves Character to selected Tile, using x,y coordinates
    def move(self, x, y):
        self.location = (x, y)

    # Each turn, increment the energy of all characters by their energy_gain
    def energy_tick(self):
        self.energy += self.energy_gain

    # Print out a list of items character is holding
    def print_items(self):
        for x in range(len(self.items)):
            print(self.items[x].description)

# Thief characters:  Sneak into the base and steal treasures to win rounds
class Thief(Character):
    dead = False

# Guard characters: Prevent thieves from breaking in to win rounds
class Guard(Character):
    # List of tiles that are lighted up by character
    light_area = []
