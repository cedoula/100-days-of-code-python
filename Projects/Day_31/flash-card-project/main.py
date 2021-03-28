from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
try:
    french_words_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_df = pd.read_csv("data/french_words.csv")
french_words_list = french_words_df.to_dict(orient="records")
english_word = ""

# ------------------------- SHOW NEXT CARD ---------------------------- #
def next_card(*args):
    global CARD_FRONT_IMG, english_word, flip_timer, french_words_list
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=CARD_FRONT_IMG)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    current_card = choice(french_words_list)
    french_word = current_card["French"]
    english_word = current_card["English"]    
    canvas.itemconfig(canvas_word, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)

    #If user knew the word the card is removed from the list    
    if len(args) > 0:
        if args[0]:
            french_words_list.remove(current_card)
            words_to_learn_df = pd.DataFrame.from_records(french_words_list, columns=["French", "English"])
            words_to_learn_df.to_csv("data/words_to_learn.csv", index=False)

# --------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global CARD_BACK_IMG, english_word
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=CARD_BACK_IMG)
    canvas.itemconfig(canvas_word, text=english_word, fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#Initialize timer and backgrounds
flip_timer = window.after(3000, func=flip_card)
CARD_FRONT_IMG = PhotoImage(file="images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=CARD_FRONT_IMG)
canvas.grid(column=0, row=0, columnspan=2)
canvas_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
next_card()


#Wrong button 
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=lambda: next_card(False))
wrong_button.grid(column=0, row=1)
#Right button 
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=lambda: next_card(True))
right_button.grid(column=1, row=1)

window.mainloop()