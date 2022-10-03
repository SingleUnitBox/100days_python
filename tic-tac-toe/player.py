class Player:

    def __init__(self, choice):
        self.symbol = choice


    def make_move(self, choice):
        self.spot = int(input(f"where you would like to put {choice} (1-9): "))
        return self.spot-1