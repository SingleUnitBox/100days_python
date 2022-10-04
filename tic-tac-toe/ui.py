from tkinter import *
from board import Board
from player import Player
from functools import partial

class BoardInterface:

    def __init__(self):
        self.all_buttons = []
        self.window = Tk()
        self.window.title("Welcome to Tic-Tac-Toe Game")
        self.choose_symbol()
        self.window.mainloop()



    def choose_symbol(self):
        self.label = Label(text="Choose X/O", font=("Arial", 20, "normal"))
        self.label.grid(row=0, column=0)
        self.button_x = Button(font=('Arial', '10'), height=5, width=10, command=lambda: self.button_clicked(self.button_x))
        self.button_x["text"] = "X"
        self.button_x.grid(row=1, column=0)
        self.button_o = Button(text="O", font=('Arial', '10'), height=5, width=10, command=lambda: self.button_clicked(self.button_o))
        self.button_o.grid(row=1, column=1)

    def button_clicked(self, button):
        if button["text"] == "X":
            self.label.config(text="X selected")
        else:
            self.label.config(text="O selected")
        self.button_x.destroy()
        self.button_o.destroy()
        self.print_board()





    def print_board(self):
        index = 0
        for i in range(1,4):
            for j in range(1,4):
                self.button = Button(text=index, font=('Arial', '10'), height=5, width=10, command=partial(self.select_square, index))
                self.button.grid(row=i, column=j)
                self.all_buttons.append(self.button)
                index += 1


    def select_square(self, index):
        #print(index)
        self.bname = (self.all_buttons[index])
        self.bname["text"] = index*2


b = BoardInterface()











# self.button1 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button1.grid(row=0, column=0)
# self.button2 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button2.grid(row=0, column=1)
# self.button3 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button3.grid(row=0, column=2)
# self.button4 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button4.grid(row=1, column=0)
# self.button5 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button5.grid(row=1, column=1)
# self.button6 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button6.grid(row=1, column=2)
# self.button7 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button7.grid(row=2, column=0)
# self.button8 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button8.grid(row=2, column=1)
# self.button9 = Button(height=5, width=10, command=self.select_square, text="", font=('Arial', '10'))
# self.button9.grid(row=2, column=2)