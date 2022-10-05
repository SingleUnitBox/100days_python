class Player:

    def __init__(self):
        self.symbol = ""


    def make_move(self, choice):
        self.spot = int(input(f"where you would like to put {choice} (1-9): "))
        return self.spot-1

    def choose_symbol(self):
        if self.choice == x_or_o:
            switch = True
        else:
            switch = False

    def store_symbol(self, symbol):
        self.symbol = symbol
