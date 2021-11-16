# Dictionary of item IDs
item_dictionary = {
0: "Boots of Speed - Run faster",
1: "Lucky Spoon - ???",
2: "Machete - Chop chop chop"
}

#Items that characters equip
class Item:
    def __init__ (self, id, cost):
        self.id = id
        self.cost = cost
        self.description = item_dictionary.get(id)
