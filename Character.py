#Character class

class Character:

    # Universal Character Attributes
    def __init__(self, l, m, v, v_r, e, e_g):
        self.location = l
        self.movement = m
        self.vision = v
        self.vision_range = v_r
        self.energy = e
        self.energy_gain = e_g

    # Testing
    def printMovement(self):
        print(self.movement)

    # Moves Character to selected Tile, using x,y coordinates
    def Move(self, x, y):
        pass
