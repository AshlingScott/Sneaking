# Main, includes user input and testing functions

from Map import *
from Unit import *
from ThiefClasses import *
from GuardClasses import *
from Item import *
from Alter import *
from Summons import *

# Various tests
def test():
    pass

# Prompt to choose a character
def char_select():
    char = input("Choose your Character - Druid, Shadow, Golem, Techie\n")
    if (char == "Druid"):
        return Druid(52)
    elif (char == "Shadow"):
        return Shadow(52)
    elif (char == "Golem"):
        return Golem(52)
    elif (char == "Techie"):
        return Techie(52)
    else:
        # If invalid input, re-enter char_select
        print("Not a valid character")
        char_select()

# Prompt to choose a tile to move to
def move_prompt():
    try:
        # Tries if a valid int is input
        choice = int(input("Move to tile - Input tile id (0 to 99)"))
        # Try to make move, return failed if terrain blocks movement
        failed = current_char.move(map, choice)
    except:
        # Give error message and recurse move
        print("Invalid - Input a number 0 to 99")
        move_prompt()
        return
    if isinstance(choice, int):
        # If move was a failure, recurse move
        if failed:
            move_prompt()

current_char = char_select()
print("\n")

test_summon = Wolf(3, current_char)
current_char.print_stats()

test_alter = Speed(True, 0, True, current_char, 2)
current_char.alters.append(test_alter)
current_char.upkeep()

print("\nUpkeep runs\n")
current_char.print_stats()

map = Map("Horseshoe")
map.print_map()
move_prompt()
map.print_map()

current_char.update_vision(map)
