import random


class Computer:

    def __init__(self, choice):
        self.symbol = choice

    def make_move(self):
        self.spot = random.randint(1, 9)
        return self.spot-1