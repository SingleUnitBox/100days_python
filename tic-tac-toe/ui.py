from tkinter import *
from functools import partial
import random


class BoardInterface:

    def __init__(self):
        self.player_symbol = ""
        self.computer_symbol = ""
        self.switch = True
        self.all_buttons = []
        self.counter = 0
        self.window = Tk()
        self.window.title("Welcome to Tic-Tac-Toe Game")
        self.choose_symbol()
        self.window.mainloop()

    def choose_symbol(self):
        self.label = Label(text="Choose X/O", font=("Arial", 20, "normal"), justify=LEFT)
        self.label.grid(row=0, column=0, columnspan=3)
        self.button_x = Button(font=('Arial', '10'), height=5, width=10, command=lambda: self.display_symbol(self.button_x["text"]))
        self.button_x["text"] = "X"
        self.button_x.grid(row=1, column=0)
        self.button_o = Button(text="O", font=('Arial', '10'), height=5, width=10, command=lambda: self.display_symbol(self.button_o["text"]))
        #lambda: self.player.store_symbol(self.button_x["text"]))
        self.button_o.grid(row=1, column=1)



    def display_symbol(self, symbol):
        self.player_symbol = symbol
        self.label.config(text=f"{self.player_symbol} selected")
        self.button_x.destroy()
        self.button_o.destroy()
        if symbol == "X":
            self.computer_symbol = "O"
        else:
            self.computer_symbol = "X"
        self.print_board()


    def print_board(self):
        index = 0
        for i in range(1,4):
            for j in range(1,4):
                self.button = Button(text="", font=('Arial', '10'), height=5, width=10, command=partial(self.select_square, index))
                self.button.grid(row=i, column=j-1)
                self.all_buttons.append(self.button)
                index += 1

    def select_square(self, index):
        self.switch = True
        #print(index)
        self.bname = self.all_buttons[index]
        if self.bname["text"] == "":
            self.bname["text"] = self.player_symbol
            if self.counter < 4:
                self.computer_square()
        if self.check_for_win():
            for button in self.all_buttons:
                button.config(state="disabled")



    def computer_square(self):
        while self.switch:
            random_square = random.choice(self.all_buttons)
            if random_square["text"] == "":
                random_square["text"] = self.computer_symbol
                self.switch = False
                self.counter += 1

    def check_for_win(self):
        list_0 = [self.all_buttons[0]["text"], self.all_buttons[1]["text"], self.all_buttons[2]["text"]]
        list_1 = [self.all_buttons[3]["text"], self.all_buttons[4]["text"], self.all_buttons[5]["text"]]
        list_2 = [self.all_buttons[6]["text"], self.all_buttons[7]["text"], self.all_buttons[8]["text"]]
        list_3 = [self.all_buttons[0]["text"], self.all_buttons[3]["text"], self.all_buttons[6]["text"]]
        list_4 = [self.all_buttons[1]["text"], self.all_buttons[4]["text"], self.all_buttons[7]["text"]]
        list_5 = [self.all_buttons[2]["text"], self.all_buttons[5]["text"], self.all_buttons[8]["text"]]
        list_6 = [self.all_buttons[0]["text"], self.all_buttons[4]["text"], self.all_buttons[8]["text"]]
        list_7 = [self.all_buttons[2]["text"], self.all_buttons[4]["text"], self.all_buttons[6]["text"]]
        list = [list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7]
        for l in list:
            if l[0] == l[1] == l[2] == "X":
                self.label.config(text=f"X won")
                return True
            elif l[0] == l[1] == l[2] == "O":
                self.label.config(text=f"O won")
                return True
        # if self.is_board_full():
        #     print("Draw")
        #     return True

