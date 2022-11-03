BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
current_card = {}
to_learn = {}
to_learn2 = {}

from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    data_frame = pandas.DataFrame(to_learn)
    data_frame.to_csv("./data/words_to_learn.csv", index=False)
    next_word()



def next_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")




window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=562, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_back = PhotoImage(file="./images/card_back.png")

canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
right = Button(image=right_img, highlightthickness=0, command=is_known)
right.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong.grid(column=0, row=1)

next_word()
















window.mainloop()
