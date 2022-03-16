# Rosters are collections of Units.  A Team is a selection of Units
# from a roster for a given game/mission/map

from Unit import *

class Roster:
    # Max number of units on a roster
    maximum = 10
    # List of units on roster
    unit_list = []

    def __init__(self):

    def create_team(self, selected_units):
