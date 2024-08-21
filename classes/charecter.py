import random


class Character:
    def __init__(self):
        self.name = "Hero"
        self.health = 100
        self.attack = 10
        self.defense = 5

    def generate_name(self):
        names = ["Hero", "Villain", "Goblin", "Dragon"]
        return random.choice(names)

    def generate_stat(self):
        return random.randint(1, 20)
