from tkinter import *
from tkinter import messagebox

DEFAULT_EMAIL = "kevinngx625@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random
import pyperclip

def generate_password():
    print("Generating password...")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.delete(0, 'end')
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    confirmation = messagebox.askokcancel(title=website, message=f"Website: {website}\nEmail/Username: {email}\nPassword:{password}")
    if (confirmation):
        details = f"{website} | {email} | {password}\n"

        with open('passwords.txt', 'a') as reader:
            reader.write(details)

        print("Adding password...")
    print(details)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# 1. Website
web_label = Label(text="Website:")
web_label.grid(column=1, row=2)

web_entry = Entry(width=35)
web_entry.grid(column=2, row=2, columnspan=2)
web_entry.focus()

# 2. Email / Username
email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

email_entry = Entry(width=35)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(END, DEFAULT_EMAIL)

# 3. Password
pass_label = Label(text="Password:")
pass_label.grid(column=1, row=4)

pass_entry = Entry(show="*", width=20)
pass_entry.grid(column=2, row=4)

# Buttons
gen_button = Button(text="Generate Password", width=11, command=generate_password)
gen_button.grid(column=3, row= 4)

add_button = Button(text="Add", width=33, command=add_password)
add_button.grid(column=2, row= 5, columnspan=2)

window.mainloop()