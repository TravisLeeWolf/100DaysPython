import tkinter

window = tkinter.Tk()
window.title("My first TKinter Window")
window.minsize(width=800, height=600)

myLabel = tkinter.Label(text="I am a label.", font=("Arial", 24))
myLabel.pack()


# This goes at the end
window.mainloop()