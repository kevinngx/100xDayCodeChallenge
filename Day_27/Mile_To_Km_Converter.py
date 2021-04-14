from tkinter import *

window = Tk()
window.title("Miles to Kilometres Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# 1. Label

my_label = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=2)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=3, row=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=3, row=2)

# 2. Button

def convert(input):
    miles = float(input)
    kilometres = miles * 1.609344
    return kilometres

def button_clicked():
    conversion = convert(input.get())
    result.config(text=conversion)

button = Button(text="Convert", command=button_clicked)
button.grid(column=2, row=3)

# 3. Entry
def print_input():
    print(input.get())
input = Entry()
input.config(width=10)
input.grid(column=2, row=1)

# 4. Result
result = Label(text="", font=("Arial", 24, "bold"))
result.grid(column=2, row=2)

window.mainloop()