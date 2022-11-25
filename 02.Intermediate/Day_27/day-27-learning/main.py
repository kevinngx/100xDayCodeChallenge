from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# 1. Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=1, row=1)
my_label["text"] = "This is a new text value"

# 2. Button
def button_clicked():
    # my_label["text"] = "I got clicked"
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=2)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=3, row=1)

# 3. Entry
def print_input():
    print(input.get())

input = Entry()
input.config(width=10)
# input.pack()
input.grid(column=4, row=3)

# Keep this line at the end
window.mainloop()