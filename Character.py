#Character class.  Characters can be either Thieves, or Guards
class Character:

    visible = False
    disabled = False
    flying = False
    has_treasure = False
    # Stealth value 0 is fully visible, 1 is light invis, 2 is heavy invis
    stealth = 0
    # List of tiles that are visible by character
    visible_tiles = []


    # Universal Character Attributes
    def __init__(self, l, m, v, e, e_g):
        self.location = l
        self.movement = m
        self.vision = v
        self.energy = e
        self.energy_gain = e_g

    # Testing
    def printMovement(self):
        print(self.movement)

    # Moves Character to selected Tile, using x,y coordinates
    def Move(self, x, y):
        pass

#Thief characters:  Sneak into the base and steal treasures to win rounds
class Thief(Character):
    dead = False

#Guard characters: Prevent thieves from breaking in to win rounds
class Guard(Character):
    # List of tiles that are lighted up by character
    light_area = []
