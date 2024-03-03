from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Reading csv file and data manipulation
data = pandas.read_csv("data/french_words.csv")
learn = data.to_dict(orient="records")
current_card = random.choice(learn)


def next_card():
    global current_card
    current_card = random.choice(learn)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    window.after(3000, change_image)


def change_image():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, change_image)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
r_button_img = PhotoImage(file="images/right.png")
r_button = Button(image=r_button_img, highlightthickness=0, command=next_card)
r_button.grid(column=0, row=1)

w_button_img = PhotoImage(file="images/wrong.png")
w_button = Button(image=w_button_img, highlightthickness=0, command=next_card)
w_button.grid(column=1, row=1)

next_card()

window.mainloop()
