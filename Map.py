#contains classes for all resources used by Characters

# Tiles are locations on the grid map.  Characters always occupy a Tile.
# Different kind of tiles have different movement and vision rules
class Tile:

    occupied = False

    # X and y are the x,y coordinates of the tile on the map.
    #Type is which type of tile it is
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type


# Maps consist of a grid of Tiles
class Map:
    def __init__(self, tile_list):
        self.tile_list = tile_list
