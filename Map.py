# Contains classes used for making and displaying the map and tile grid

from random import randrange
import csv

# Tiles are locations on the grid map.  Characters always occupy a Tile.
# Different kind of tiles have different movement and vision rules
class Tile:
    # Whether a tile has a Character on it
    occupied = False

    # ID is the id of the tile in the maps tile_list
    # Type is which type of tile it is.  0 is grass, 1 is forest, 2 is rock
    # Occupant is a unit standing on the tile
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.occupant = None

# Maps consist of a grid of Tiles
# Can generate maps from csv files, or completely randomise them
# Use string filename for csv, any int for random
class Map:
    def __init__(self, *args):
        self.tile_list = []
        print("\n")
        # Tries to load map from CSV file
        if isinstance(args[0], str):
            try:
                with open("MapFiles/" + args[0] + ".csv", 'r') as file:
                    csvreader = csv.reader(file)
                    for y in range(10):
                        line = next(csvreader)
                        for x in range(10):
                            self.tile_list.append(Tile((y * 10 + x ), int(line[x])))

                # Names the map
                self.name = args[0]
            except:
                print("Invalid file - Cannot load map")

        # If non-string argument, randomly generates a map instead
        else:
            print("\n")
            y = 0
            for x in range(100):
                x += 1
                # Give triple chance for fields to spawn
                z = randrange(0,5)
                if (z == 3) or (z == 4):
                    z = 0
                if (x == 10):
                    x = 0
                    y += 1
                self.tile_list.append(Tile((y*10 + x), z))

            # Names the map
            self.name = "Random Map"

    # Prints out the map as an array of 10x10
    # Prints character symbols on occupied space, tile type on empty space
    def print_map(self):
        for y in range(10):
            map_line = ""
            for x in range(10):
                if (self.tile_list[(y * 10 + x)].occupied == True):
                    map_line+=self.tile_list[(y * 10 + x)].occupant.get_symbol() + " "
                else:
                    map_line += str(self.tile_list[(y * 10 + x)].type) + " "
            print(map_line)

    # Simplifies the map by reducing the value of each tiles type, min of 0
    def simplify(self):
        for x in range(100):
            if (self.tile_list[x].type > 0):
                self.tile_list[x].type -= 1

    # Return a set of tiles in a square, within a range of target tile
    # Used on vision ranges, potential movements, ability targetting
    def grab_square(self, map, target, _range_):
        tileset = []
        # Sets the squares borders
        for x in range(-_range_, _range_ + 1):
            for y in range(-_range_, _range_ + 1):
                # Check that x value is between 0 and 9
                a = int(target.id / 10) + x
                if (0 <= a < 10):
                    # Check that y value is between 0 and 9
                    b = int(target.id % 10) + y
                    if (0 <= b < 10):
                        # Add tile after all criteria met
                        tileset.append(map.tile_list[(a * 10) + b])

        return tileset
