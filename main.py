from tkinter import *
import pandas
import random

# Constants and variables
 
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
rand_word = ""
words_to_learn = []


# Functions

def change_word():
    global rand_word
    canvas.itemconfig(lang, text="French")
    rand_word = random.choice(data)
    canvas.itemconfig(word, text=rand_word["French"])
    canvas.itemconfig(card, image=card_front)
    window.after(3000, show_translation)


def show_translation():
    global rand_word
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(lang, text="English")
    canvas.itemconfig(word, text=rand_word["English"])


def right_click():
    data.remove(rand_word)
    change_word()


def wrong_click():
    words_to_learn.append(rand_word)
    change_word()


# UI Setup

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=wrong_click)
wrong.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, highlightthickness=0, command=right_click)
right.grid(row=1, column=1)

change_word()

window.mainloop()

pandas.DataFrame(words_to_learn).to_csv(path_or_buf="data/words_to_learn.csv")
