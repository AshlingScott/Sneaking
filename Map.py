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
    # Loads a map from a csv file
    def __init__(self, *args):
        self.tile_list = []
        if isinstance(args[0], str):
            rows = []
            with open("MapFiles/" + args[0] + ".csv", 'r') as file:
                csvreader = csv.reader(file)
                for y in range(10):
                    line = next(csvreader)
                    for x in range(10):
                        self.tile_list.append(Tile((y * 10 + x ), int(line[x])))

        # If non-string argument, randomly generates a map instead
        else:
            random_list = []
            x = 0
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
                random_list.append(Tile((y*10 + x), z))

            self.tile_list = random_list

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

    # Return a set of tiles in a square, within a range of target tile
    def grab_square(self, map, target, _range_):
        tileset = set()
        # Sets the squares borders
        for a in range(-_range_, _range_ + 1):
            for b in range(-_range_, _range_ + 1):
                # Check that x value is between 0 and 9
                x = int(target.id / 10) + a
                if (0 <= a < 10):
                    # Check that y value is between 0 and 9
                    y = int(target.id % 10) + b
                    if (0 <= b <= 10):
                        # Add tile after all criteria met
                        tileset.add(map.tile_list[(y * 10) + x])

        return tileset
