# Main, includes user input and testing functions

from Map import *
from Unit import *
from ThiefClasses import *
from GuardClasses import *
from Item import *
from Alter import *
from Summons import *
from Talents import *
from Roster import *

# Prompt to choose a character
def char_select() -> None:
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
def move_prompt(current_unit: Unit) -> None:
    try:
        # Tries if a valid int is input
        choice = int(input("Move to tile - Input tile id (0 to 99)"))
        # Try to make move, return failed if terrain blocks movement
        failed = current_unit.move(map, choice)
    except:
        # Give error message and recurse move
        print("Invalid - Input a number 0 to 99")
        move_prompt(current_unit)
        return
    if isinstance(choice, int):
        # If move was a failure, recurse move
        if failed:
            move_prompt(current_unit)

# Prompt to choose an item to aquire and equip
def item_prompt(current_unit: Unit) -> None:
    choice = input("Choose an item:\n1 - Boots of speed\n2 - Spyglass\
        3 - Tri Charm Amulet")
    if (choice == "1"):
        current_unit.add_item(Boots(current_unit))
    elif (choice == "2"):
        current_unit.add_item(Spyglass(current_unit))
    elif (choice == "3"):
        current_unit.add_item(Tri_Charm_Amulet(current_unit))
    else:
        print("Not a valid choice, choose 1 to 3")
        item_prompt(current_unit)

# Prompt to select an ability to use
# Sends map along with the choice, as many abilities need the map to work
def ability_prompt(current_unit: Unit) -> None:
    current_unit.print_abilities()
    choice = input("Choose an ability to perform, or hit x to cancel")
    # If choice is x, return to options
    # If ability is otherwise invalid, return invalid and re-enter function
    if (choice == "x"):
        select_option(current_unit)
    else:
        if (current_unit.ability_selection(map, choice) == "invalid"):
            ability_prompt(current_unit)

# Choose which action to perform next
def select_option(current_unit: Unit) -> None:
    map.print_map()
    choice = input("Choose an option:\n1 - Move\n2 - Get Item\n3 - Use ability\n")
    if (choice == "1"):
        move_prompt(current_unit)
    elif (choice == "2"):
        item_prompt(current_unit)
    elif (choice == "3"):
        ability_prompt(current_unit)
    else:
        print("Not a valid choice, choose 1 to 3")
        select_option(current_unit)

# A turn involves running upkeep on the current unit, then letting them choose
# an action to take.  They are sent to the back of the queue afterwards
def turn() -> None:
    current_unit = unit_list[0]
    current_unit.upkeep()
    select_option(current_unit)

    # Move unit to the back of the queue
    unit_list.pop(0)
    unit_list.append(current_unit)

# TESTING

# Create talent tree
talent_tree = TalentTree()

# Create Roster
roster = Roster()

# Select character then add to Roster
chosen = char_select()
print("\n")
roster.add_unit(chosen)

test_summon = Wolf(3, chosen)
chosen.print_stats()

test_alter = Speed(True, 0, True, chosen, 2, "testing")
chosen.alters.append(test_alter)
chosen.upkeep()

print("\nUpkeep runs\n")
chosen.print_stats()

map = Map("Horseshoe")

chosen.update_vision(map)

chosen.upkeep()
chosen.print_stats()

# Unit list is a queue that shows the order of turns coming up
unit_list = []
unit_list.append(chosen)

turn()
