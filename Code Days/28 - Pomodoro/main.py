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
REPS = 0
POMO_TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    global REPS
    window.after_cancel(POMO_TIMER)
    REPS = 0
    canvas.itemconfig(timerText, text="00:00")
    titleLabel.config(text="Timer", fg=GREEN)
    pomoPartDoneLabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global REPS
    workMinutes = WORK_MIN * 60
    shortBreakMinutes = SHORT_BREAK_MIN * 60
    longBreakMin = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS == 8:
        countDown(longBreakMin)
        titleLabel.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        countDown(shortBreakMinutes)
        titleLabel.config(text="Break", fg=PINK)
    else:
        countDown(workMinutes)
        titleLabel.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    countMinutes = math.floor(count / 60)
    if countMinutes < 10:
        countMinutes = "0" + str(countMinutes)
    countSecconds = count % 60
    if countSecconds == 0:
        countSecconds = "00"
    elif countSecconds < 10:
        countSecconds = "0" + str(countSecconds)
    canvas.itemconfig(timerText, text=f"{countMinutes}:{countSecconds}")
    if count > 0:
        global POMO_TIMER
        POMO_TIMER = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        checkMarks = ""
        workParts = math.floor(REPS/2)
        for _ in range(workParts):
            checkMarks += "✔"
        pomoPartDoneLabel.config(text=checkMarks)

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
resetButton = Button(text="Reset", font=(FONT_NAME, 15), command=resetTimer)
resetButton.grid(column=2, row=2)

# 25 min completed label ⏱✔
pomoPartDoneLabel = Label(font=(FONT_NAME, 20, "bold",), fg=GREEN, bg=YELLOW )
pomoPartDoneLabel.grid(column=1, row=3)


# Goes at the end so the window doesn't automatically close
window.mainloop()