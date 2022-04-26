# Talents are the bonuses characters earn from levelling up
# Talents can be active abilities or passive buffs

import json
from abc import *

class Talent(ABC):

    def __init__(self, id: int, name: str, description: str, active: bool,
            tier: int, effects: list, connections: list):
        self.id = id
        self.name = name
        self.description = description
        self.active = active
        self.tier = tier
        self.effects = effects
        self.connections = connections

class TalentTree:

    def __init__(self):
        # List of Talents
        talent_tree = []

        # Load talent tree from json
        file = open("Data/Talents/TalentTree.json")
        data = json.load(file)

        # Put talents into the talent tree list
        for x in data["talents"]:
            self.talent_tree.append(Talent(x["id"], x["name"], x["description"],
            x["active"], x["tier"], x["effects"], x["connections"]))

    # returns list of talents
    def get_list():
        return self.talent_tree
