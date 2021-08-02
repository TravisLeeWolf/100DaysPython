import tkinter

window = tkinter.Tk()
window.title("Labels & Buttons")
window.minsize(width=640, height=480)

# Label
myLabel = tkinter.Label(text="I'm a label.", font=("Arial", 24))
myLabel.grid(column=0, row=0)

# Button
def buttonClicked():
    inputText = myInput.get()
    myLabel.config(text=inputText)

myButton = tkinter.Button(text="Add Text", command=buttonClicked)
myButton.grid(column=1, row=1)

# New Button
def newButtonClicked():
    myLabel.config(text="I've been clicked!")

myNewButton = tkinter.Button(text="Click Me", command=newButtonClicked)
myNewButton.grid(column=2, row=0)

# Input
myInput = tkinter.Entry(width=12)
myInput.grid(column=3, row=2)

# Goes at the end, don't forget
window.mainloop()