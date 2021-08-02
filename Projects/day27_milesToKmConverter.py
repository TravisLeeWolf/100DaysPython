import tkinter

FONT = ("Pokemon GB", 16)

window = tkinter.Tk()
window.title("Labels & Buttons")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# NOTE: Grid layout is 3x3

# User input grid[1,0] get miles
milesInput = tkinter.Entry(width=10, font=FONT, justify="center")
milesInput.grid(column=1, row=0)

# Label grid[2,0] "Miles"
milesLabel = tkinter.Label(text="Miles", font=FONT)
milesLabel.grid(column=2, row=0)

# Label grid[0,1] "is equal to"
equalsLabel = tkinter.Label(text="is equal to", font=FONT)
equalsLabel.grid(column=0, row=1)

# Label grid[1,1] display result in km
kmResultLabel = tkinter.Label(text="0", font=FONT)
kmResultLabel.grid(column=1, row=1)

# Label grid[2,1] "Km"
kmLabel = tkinter.Label(text="KM", font=FONT)
kmLabel.grid(column=2, row=1)

# Button grid[1,2] Calculate
def converToKm():
    inputValue = int(milesInput.get())
    kmConversion = inputValue * 1.609344
    kmResultLabel.config(text=str(round(kmConversion, 2)))
myButton = tkinter.Button(text="Calculate", command=converToKm, font=FONT)
myButton.grid(column=1, row=2)


# Goes at the end, don't forget
window.mainloop()