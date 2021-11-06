#Items that characters equip

# Item base class
class Item:

    def __init__ (self, id, cost):
        self.id = id
        self.cost = cost

class Treasure(Item):

    def __init__ (self):
