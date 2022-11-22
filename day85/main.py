import tkinter as tk
import random
import time

word_list = ["lumber", "talented", "successful", "worthless", "arrange", "luxuriant", "unadvised", "stay", "rings",
             "proud", "freezing", "pastoral", "wrathful", "faded", "melted", "zippy", "harm", "nutty", "jump",
             "condemned", "grain", "angry", "alert", "bike", "rescue", "river", "floor", "borrow", "guess", "push",
             "preserve", "crooked", "unpack", "pause", "lock", "breezy", "room", "damaged", "telling", "mark", "nest",
             "tremble", "continue", "can", "servant", "lamp", "design", "tree", "legs", "boundless"]
counter = 0
i = 0
words_per_minute = 0
correct_words = 0
timer = 60




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

label_words = tk.Label(text=f"correct words: {correct_words}", font=("Arial", 20, "bold"))
label_words.grid(column=0, row=2)

label_timer = tk.Label(text=f"60", font=("Arial", 20, "bold"))
label_timer.grid(column=0, row=3)


input = tk.Entry(width=50, justify="center", font=("Arial", 20, "bold"))
input.grid(column=0, row=1)

def my_function(self):
    global i
    global counter
    global words_per_minute
    global correct_words
    input_word = str(input.get()).strip()
    if i == len(word_list):
        print("you are done")
    else:
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
            correct_words += 1
            label_words.config(text=f"correct words: {correct_words}")
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
def count_down(count):
    if count >= 1:
        root.after(1000, count_down, count - 1)
        label_timer.config(text=f"{count}")
    else:
        label_timer.config(text=f"0")
        words_per_minute_label = tk.Label(text=f"You have typed {correct_words} per minute", font=("Arial", 20, "bold"))
        words_per_minute_label.grid(column=0, row=4)


timer = count_down(60)


root.mainloop()


