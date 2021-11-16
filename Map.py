from random import randrange

# Contains classes used for making and displaying the map and tile grid
# Tiles are locations on the grid map.  Characters always occupy a Tile.
# Different kind of tiles have different movement and vision rules
class Tile:
    # Whether a tile has a Character on it
    occupied = False

    # X and y are the x,y coordinates of the tile on the map.
    # Type is which type of tile it is.  0 is grass, 1 is forest, 2 is rock
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

# Maps consist of a grid of Tiles
# Currently generates a random map
class Map:
    def __init__(self):
        tile_list = []
        x = 0
        y = 0
        for x in range(100):
            x += 1
            if (x == 10):
                x = 0
                y += 1

            #tile = Tile(x, y, randrange(0,3))
            tile_list.append(Tile(x, y, randrange(0,3)))

        self.tile_list = tile_list

    # Prints out the map as an array of 10x10
    def print_map(self):
        for y in range(10):
            map_array = ""
            for x in range(10):
                map_array = map_array + " " + str(self.tile_list[(y*10) + x].type)
            print(map_array)

    # Simplifies the map by reducing the value of each tiles type, min of 0
    def simplify(self):
        for x in range(100):
            if (self.tile_list[x].type > 0):
                self.tile_list[x].type -= 1
