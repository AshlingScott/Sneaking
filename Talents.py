# Talents are the bonuses characters earn from levelling up
# Talents can be active abilities or passive buffs

import json
from abc import *

class Talent(ABC):
    # The talents that link to this talent
    connections = []

    def __init__(self, name: str, description: str, active: bool,
            tier: int, effects: list):
        self.name = name
        self.description = description
        self.active = active
        self.tier = tier
        self.effects = effects

class TalentTree:

    def __init__(self):
        # List of Talents
        talent_tree = []

        # Load talent tree from json
        file = open("Data/TalentTree.json")
        data = json.load(file)

        # Put talents in talent tree list
        for x in data["talents"]:
            y = Talent(x["name"], x["description"], x["active"], x["tier"], x["effects"])
            talent_tree.append(y)

        # Links talents together
        # TODO

    # returns list of talents
    def get_list():
        return talent_tree
