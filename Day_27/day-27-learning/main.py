import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")


# # Using turtle
# import turtle
# tim = turtle.Turtle()
# tim.write("Hello, World!")




# Keep this line at the end
window.mainloop()