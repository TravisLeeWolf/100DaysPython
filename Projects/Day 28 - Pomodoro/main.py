from tkinter import *
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    countDown(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    countMinutes = math.floor(count / 60)
    countSecconds = count % 60
    canvas.itemconfig(timerText, text=f"{countMinutes}:{countSecconds}")
    if count > 0:
        window.after(1000, countDown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Adding the tomato picture to our window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title Text
titleLabel = Label(text="Timer", font=(FONT_NAME, 35, "bold",), fg=GREEN, bg=YELLOW)
titleLabel.grid(column=1, row=0, sticky="s")

# Start button
startButton = Button(text="Start", font=(FONT_NAME, 15), command=startTimer)
startButton.grid(column=0, row=2)

# Reset button
resetButton = Button(text="Reset", font=(FONT_NAME, 15))
resetButton.grid(column=2, row=2)

# 25 min completed label ⏱✔
pomoDoneLabel = Label(text="[✔]", font=(FONT_NAME, 20, "bold",), fg=GREEN, bg=YELLOW )
pomoDoneLabel.grid(column=1, row=3)


# Goes at the end so the window doesn't automatically close
window.mainloop()