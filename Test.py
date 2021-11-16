#testing
from Map import *
from Character import *
from ThiefClasses import *
from GuardClasses import *
from Item import *
from Alter import *

map = Map()
map.print_map()
map.simplify()
print("   ")
map.print_map()

chara = Character(5, 5, 2, 3, 5)

druwu = Druid(0, 0, 5, 3, 5)
print(druwu.form)

shadowu = Shadow(0, 9, 8, 7, 5)
shadowu.shadow_dance()
print(shadowu.energy)

print(shadowu.disabled)
druwu.entangle(shadowu)
print(shadowu.disabled)

huntu = Blood_hunter(9, 0, 3, 4, 5)
huntu.blood_scent()
print(huntu.energy)

golu = Golem(9, 9, 4, 5, 6)

print(druwu.location)
print(golu.location)
golu.move(map, 9, 8)
print(golu.location)

druwu.items.append(Item(1, 0))
druwu.print_items()
druwu.items.append(Item(0, 0))
druwu.print_items()

druwu.alter.append(Alter(False, 2, True))
druwu.upkeep()
druwu.upkeep()
druwu.upkeep()
druwu.upkeep()
