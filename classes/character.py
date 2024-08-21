import random
from data.names import names


class Character:
    def __init__(self):
        self.name = "name: " + self.generate_name()
        self.health = self.generate_stat()
        self.attack = self.generate_stat()
        self.defense = self.generate_stat()

    def generate_name(self):
        return random.choice(names)

    def generate_stat(self):
        return random.randint(1, 20)
