import random
import os
from board import Board
from player import Player
from computer import Computer
from tkinter import *

list = ["x", "o"]
x_or_o = random.choice(list)
game_is_on = True

window = Tk()
window.title("Welcome to Tic-Tac-Toe Game")




board = Board()
board.print_board()
choice = input("Choose your symbol: (X/O): ").lower()
if choice == x_or_o:
    switch = True
else:
    switch = False
player = Player(choice)
list.remove(choice)
com_choice = list[0]
computer = Computer(com_choice)
print(f"'{x_or_o.upper()}' begins: ")
board.clear_board()
board.print_board()

while game_is_on:
    if board.check_for_win():
        game_is_on = False
    else:
        if switch:
            move = player.make_move(choice)
            if board.is_spot_empty(move):
                board.update_board(move, choice)
                board.print_board()
                switch = False
        else:
            com_move = computer.make_move()
            if board.is_spot_empty(com_move, com_choice):
                board.update_board(com_move, com_choice)
                board.print_board()
                switch = True

