#Main, includes user input and testing methods
import os

from Map import *
from Unit import *
from ThiefClasses import *
from GuardClasses import *
from Item import *
from Alter import *

# Various tests
def test():
    print(os.listdir())

    map = Map(4)
    map.print_map()
    map = Map("Horseshoe")

    druwu = Druid(22, 5, 3, 5)
    print(druwu.form)

    druwu.print_stats()

    shadow = Shadow(45, 8, 7, 5)
    shadow.shadow_dance()
    print(shadow.energy)

    print(shadow.disabled)
    druwu.entangle(shadow)
    print(shadow.disabled)

    hunt = Blood_hunter(17, 3, 4, 5)
    hunt.blood_scent()
    print(hunt.energy)

    gol = Golem(9, 4, 5, 6)

    print(druwu.location)
    print(gol.location)
    gol.move(map, 9)
    print(gol.location)

    map.print_map()

    druwu.items.append(Item(1, 0))
    druwu.print_items()

    druwu.alter.append(Alter(False, 2, True))
    druwu.upkeep()
    druwu.upkeep()
    druwu.upkeep()

    threegrab = map.grab_square(map, map.tile_list[0], 3)
    for x in threegrab:
        print(x.id)

# Prompt to choose a character
def char_select():
    char = input("Choose your Character - Druid, Shadow, Golem, Techie\n")
    if (char == "Druid"):
        return Druid(2, 3, 2, 1)
    elif (char == "Shadow"):
        return Shadow(6, 6, 4, 9)
    elif (char == "Golem"):
        return Golem(3, 4, 5, 6)
    elif (char == "Techie"):
        return Techie(6, 4, 8, 2)
    else:
        # If invalid input, re-enter char_select
        print("Not a valid character")
        char_select()

# Prompt to choose a tile to move to
def move_prompt():
    try:
        # Tries if a valid int is input
        choice = int(input("Move to tile - Input tile id (0 to 99)"))
    except:
        # Give error message and recurse move
        print("Invalid - Input a number 0 to 99")
        move_prompt()
        return
    if isinstance(choice, int):
        # Try to make move
        failed = player_char.move(map, choice)
        # If move was a failure, recurse move
        if failed:
            move_prompt()

# Main execution
player_char = char_select()
print("\n")
player_char.print_stats()

map = Map("Horseshoe")
player_char.kill()
player_char.move(map, 42)
map.print_map()
move_prompt()
map.print_map()

player_char.get_vision(map)
