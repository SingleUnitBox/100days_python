class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def print_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("---------------------")

    def is_board_full(self):
        list = []
        for element in self.board:
            if element != " ":
                list.append(element)
                if len(list) == 9:
                    return True


    def clear_board(self):
        self.board = [f" " for x in range(9)]

    def create_board(self):
        self.board = [f"{x + 1}" for x in range(9)]

    def update_board(self, number, symbol):
            self.board[number] = symbol

    def is_spot_empty(self, number, key=None):
        if self.board[number] != "x" and self.board[number] != "o":
            return True
        elif key:
            return False
        else:
            print("please choose another spot")
            return False

    def check_for_win(self):
        list_0 = [self.board[0], self.board[1], self.board[2]]
        list_1 = [self.board[3], self.board[4], self.board[5]]
        list_2 = [self.board[6], self.board[7], self.board[8]]
        list_3 = [self.board[0], self.board[3], self.board[6]]
        list_4 = [self.board[1], self.board[4], self.board[7]]
        list_5 = [self.board[2], self.board[5], self.board[8]]
        list_6 = [self.board[0], self.board[4], self.board[8]]
        list_7 = [self.board[2], self.board[4], self.board[6]]
        list = [list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7]
        for l in list:
            if l[0] == l[1] == l[2] == "x":
                print("X won")
                return True
            elif l[0] == l[1] == l[2] == "o":
                print("O won")
                return True
        if self.is_board_full():
            print("Draw")
            return True





