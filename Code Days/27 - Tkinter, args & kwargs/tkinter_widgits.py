import tkinter

window = tkinter.Tk()
window.title("Labels & Buttons")
window.minsize(width=640, height=480)

# Label
myLabel = tkinter.Label(text="I'm a label.", font=("Arial", 24))
myLabel.pack()

# Button
def buttonClicked():
    inputText = myInput.get()
    myLabel.config(text=inputText)

myButton = tkinter.Button(text="Click Me", command=buttonClicked)
myButton.pack()

# Input
myInput = tkinter.Entry(width=12)
myInput.pack()

# Goes at the end, don't forget
window.mainloop()