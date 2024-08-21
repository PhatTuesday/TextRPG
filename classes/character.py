import random
from data.names import names
from data.races import races
from data.types import types


class Character:
    def __init__(self):
        self.name = "Name: " + self.generate_name()
        self.race = "Race: " + self.generate_race()
        self.type = "Class: " + self.generate_class()
        self.health = "HP: " + str(self.generate_stat())
        self.attack = "Attack: " + str(self.generate_stat())
        self.defense = "Defence: " + str(self.generate_stat())

    def generate_name(self):
        return random.choice(names)

    def generate_race(self):
        return random.choice(races)

    def generate_class(self):
        return random.choice(types)

    def generate_stat(self):
        return random.randint(1, 10)


