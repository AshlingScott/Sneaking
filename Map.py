from random import randrange

# Contains classes used for making and displaying the map and tile grid
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

            tile_list.append(Tile((y*10 + x), randrange(0,3)))

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
