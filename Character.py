#Character class.  Characters can be either Thieves, or Guards
class Character:

    self.visible = false
    self.disabled = false
    self.flying = false
    self.has_treasure = false
    # stealth value 0 is fully visible, 1 is light invis, 2 is heavy invis
    self.stealth = 0

    # Universal Character Attributes
    def __init__(self, l, m, v, v_t, e, e_g):
        self.location = l
        self.movement = m
        self.vision = v
        self.visible_tiles = v_t
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
    self.dead = False

#Guard characters: Prevent thieves from breaking in to win rounds
class Guard(Character):
    self.light_area = null
