class Player:

    def __init__(self, choice):
        self.symbol = choice


    def make_move(self, choice):
        self.spot = int(input(f"where you would like to put {choice} (1-9): "))
        return self.spot-1

    # def choose_symbol(self):
    #     self.choice = input("Choose your symbol: (X/O): ").lower()
    #     if self.choice == x_or_o:
    #         switch = True
    #     else:
    #         switch = False

    def select_square(self, symbol):
        return symbol