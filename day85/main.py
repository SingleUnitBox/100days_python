import tkinter as tk
import random

word_list = ["lumber", "talented", "successful", "worthless", "arrange", "luxuriant", "unadvised", "stay", "rings",
             "proud", "freezing", "pastoral", "wrathful", "faded", "melted", "zippy", "harm", "nutty", "jump",
             "condemned", "grain", "angry", "alert", "bike", "rescue", "river", "floor", "borrow", "guess", "push",
             "preserve", "crooked", "unpack", "pause", "lock", "breezy", "room", "damaged", "telling", "mark", "nest",
             "tremble", "continue", "can", "servant", "lamp", "design", "tree", "legs", "boundless"]
counter = 0
i = 0
words_per_minute = 0
correct_words_per_minute = 0


random.shuffle(word_list)


root = tk.Tk()
root.title("Typing Speed")
root.geometry("1200x400")

field = tk.Text(root, height=5, font=("Arial", 20, "bold"))
field.grid(column=0, row=0)
field.insert(tk.END, word_list)
field.configure(state="disabled")
# field.tag_add("typed_word", f"1.{counter}", f"1.{counter+len(word_list[i])}")
# field.tag_config("typed_word", background="grey")

label_timer = tk.Label(text="Timer", font=("Arial", 20, "bold"))
label_timer.grid(column=0, row=2)

input = tk.Entry(width=50, justify="center", font=("Arial", 20, "bold"))
input.grid(column=0, row=1)

def my_function(self):
    global i
    global counter
    global words_per_minute
    global correct_words_per_minute
    input_word = str(input.get()).strip()
    if input_word == word_list[i]:
        # print(input_word)
        # print(word_list[i])
        #print(f"counter: {counter} word_len: {len(word_list[i])} i: {i}")
        field.tag_add(f"typed_word{i}", f"1.{counter}", f"1.{counter+len(word_list[i])}")
        field.tag_config(f"typed_word{i}", background="green")
        counter += len(word_list[i])
        counter +=1
        # print(f"counter: {counter} word_len: {len(word_list[i])}, i: {i}")
        # field.tag_add("next_word", f"1.{counter}", f"1.{counter+len(word_list[i+1])}")
        # field.tag_config("next_word", background="gray")
        input.delete(0, "end")
        i += 1
        words_per_minute += 1
        correct_words_per_minute += 1
    else:
        #print(f"counter: {counter} word_len: {len(word_list[i])} i: {i}")
        field.tag_add(f"typed_word{i}", f"1.{counter}", f"1.{counter + len(word_list[i])}")
        field.tag_config(f"typed_word{i}", background="red")
        counter += len(word_list[i])
        counter += 1
        # print(f"counter: {counter} word_len: {len(word_list[i])}, i: {i}")
        # field.tag_add("next_word", f"1.{counter}", f"1.{counter+len(word_list[i+1])}")
        # field.tag_config("next_word", background="gray")
        input.delete(0, "end")
        i += 1
        words_per_minute += 1


root.bind("<space>", my_function)

root.mainloop()


