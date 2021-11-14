#testing
from random import randrange
from Map import *
from Character import *
from ThiefClasses import *
from GuardClasses import *

chara = Character(17, 2, 3, 4, 5)
chara.printMovement()

druwu = Druid(1, 5, 3, 4, 5)
druwu.printMovement()
print(druwu.form)

shadowu = Shadow(1, 8, 7, 6, 5)
print(shadowu.energy)
shadowu.Shadow_dance()
print(shadowu.energy)

print(shadowu.disabled)
druwu.Entangle(shadowu)
print(shadowu.disabled)

map = Map()
map.print_map()
