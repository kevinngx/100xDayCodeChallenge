BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

from tkinter import *
import csv
import random
import pandas

SAVED_FILE = "data/words_to_learn.csv"
BASE_FILE = "data/french_words.csv" 

current_card = {}

def save_progress():
    word_dict.pop(current_card["French"])
    data = pandas.DataFrame(word_dict.items(), columns=["French", "English"])
    data.to_csv(SAVED_FILE, index=False)

# Process right
def proc_right():
    print("Right Answer")
    save_progress()
    next_card()    

# Process wrong
def proc_wrong():
    print("Wrong Answer")
    next_card()
    
# ---------- Reading the CSV ---------- #

word_dict = {}

try:
    with open(SAVED_FILE) as data_file:
        data = csv.reader(data_file, delimiter=",")
        for row in data:
            if not row[0] == "French":
                word_dict[row[0]] = row[1]
    print("Saved file loaded")
except FileNotFoundError:
    with open(BASE_FILE) as data_file:
        data = csv.reader(data_file, delimiter=",")
        for row in data:
            if not row[0] == "French":
                word_dict[row[0]] = row[1]
    print("Raw file loaded")
finally:
    print("Data load successful")

# with open(BASE_FILE) as data_file:
#     data = csv.reader(data_file, delimiter=",")
#     for row in data:
#         # print(row)
#         if not row[0] == "French":
#             word_dict[row[0]] = row[1]
#     print(word_dict)
    
# ---------- Get random word pair ---------- #

def get_word():
    global current_card
    word_fr = random.choice(list(word_dict.keys()))
    word_en = word_dict[word_fr]
    word = {
        "French":word_fr,
        "English":word_en
        }
    current_card = word

def next_card():
    get_word()
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(lang_label, text="French")
    canvas.itemconfig(word_label, text=current_card["French"])  
    window.after(3000, func=flip_card)  

def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(lang_label, text="English")
    canvas.itemconfig(word_label, text=current_card["English"])  

# ---------- Set up the UI ---------- #

window = Tk()
window.title("Flashcard Game")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

# Flashcard + Label
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=1, row=1, columnspan=3)

lang_label = canvas.create_text(400, 150, text=LANGUAGE, font=LANGUAGE_FONT)
word_label = canvas.create_text(400, 263, text="WORD", font=WORD_FONT)

# Button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=proc_right, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
right_button.grid(column=1, row=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=proc_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(column=3, row=2)

next_card()
window.after(3000, flip_card)

window.mainloop()