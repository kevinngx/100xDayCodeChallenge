
from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_clicked():
    window.after_cancel(timer)
    head_label.config(text="Pomodoro")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        head_label.config(text="Long Break Time :)", fg=RED)
        countdown(long_break_sec)    
    if reps % 2 == 0:
        head_label.config(text="Short Break Time :)", fg=PINK)
        countdown(short_break_sec)
    else:
        head_label.config(text="Work Time :(", fg=GREEN)
        countdown(work_sec)

def time_text(seconds):
    min = int(seconds / 60)
    sec = seconds % 60
    if sec < 10:
        sec = f"0{sec}"
    return f"{min}:{sec}"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=75, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    canvas.itemconfig(timer_text, text=time_text(count))

    if count > 0:
        global timer 
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
             marks += "✔"
        tick_label.config(text=marks)

head_label = Label(text="Pomodoro", bg=YELLOW, font=(FONT_NAME, 35, "bold"))
head_label.grid(column=2, row=1)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_image)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 20))
canvas.grid(column=2, row=2)

start_button = Button(text="start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="reset", command=reset_clicked, highlightthickness=0)
reset_button.grid(column=3, row=3)

tick_label = Label(text="", bg=YELLOW, fg=GREEN)
tick_label.grid(column=2, row=4)


window.mainloop()
