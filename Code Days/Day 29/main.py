from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Grid layout col-3 row-5
# Setting up the window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Adding the picture to the window
canvas = Canvas(width=200, height=200)
lockImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lockImage)
canvas.grid(column=1, row=0)

# Website label grid[0,1]
websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1)

# Website input grid[1,1] colspan 2 width 35
websiteInput = Entry(width=35)
websiteInput.grid(column=1, row=1, columnspan=2)

# Email/Username label grid[0,2]
emailUsernameLabel = Label(text="Email/Username:")
emailUsernameLabel.grid(column=0, row=2)

# Email/Username input grid[1,2] colspan 2 width 35
emailUsernameInput = Entry(width=35)
emailUsernameInput.grid(column=1, row=2, columnspan=2)

# Password label grid[0,3]
passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0, row=3)

# Password input grid[1,3] width 21
passwordInput = Entry(width=21)
passwordInput.grid(column=1, row=3)

# Generate Password button grid[2,3]
generatePasswordButton = Button(text="Generate Password")
generatePasswordButton.grid(column=2, row=3)

# Add button grid[1,4] colspan 2 width 36
addToFileButton = Button(text="Add", width=36)
addToFileButton.grid(column=1, row=4)


# Goes at the end to keep the window runnung
window.mainloop()