from tkinter import *
from tkinter.messagebox import askokcancel, showwarning
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websiteText = websiteInput.get()
    emailUsernameText = emailUsernameInput.get()
    passwordText = passwordInput.get()

    if websiteText == "" or passwordText == "":
        showwarning(title="Missing Fields!", message="Please enter in all fields.")
    else:
        okayToSave = askokcancel(title="Add Entry", message=f"Website: {websiteText}\nEmail: {emailUsernameText}\nPassword: {passwordText}\nDo you want to add this entry?")
        if okayToSave:
            with open("password_manager_data.txt", mode="a") as dataFile:
                dataFile.write(f"{websiteText} | {emailUsernameText} | {passwordText}\n")
        websiteInput.delete(0, END)
        passwordInput.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Grid layout col-3 row-5
# Setting up the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="black")

# Adding the picture to the window
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
lockImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lockImage)
canvas.grid(column=1, row=0)

# Website label grid[0,1]
websiteLabel = Label(text="Website: ", fg="white", bg="black")
websiteLabel.grid(column=0, row=1)

# Website input grid[1,1] colspan 2 width 35
websiteInput = Entry(width=52)
websiteInput.grid(column=1, row=1, columnspan=2, sticky="w")
websiteInput.focus()

# Email/Username label grid[0,2]
emailUsernameLabel = Label(text="Email/Username: ", fg="white", bg="black")
emailUsernameLabel.grid(column=0, row=2)

# Email/Username input grid[1,2] colspan 2 width 35
emailUsernameInput = Entry(width=52)
emailUsernameInput.grid(column=1, row=2, columnspan=2, sticky="w")
emailUsernameInput.insert(0, "bob.builder@gmail.com")

# Password label grid[0,3]
passwordLabel = Label(text="Password: ", fg="white", bg="black")
passwordLabel.grid(column=0, row=3)

# Password input grid[1,3] width 21
passwordInput = Entry(window, width=27, show="*")
passwordInput.grid(column=1, row=3, sticky="w")

# Generate Password button grid[2,3]
generatePasswordButton = Button(text="Generate Password", fg="white", bg="darkred")
generatePasswordButton.grid(column=2, row=3, sticky="w")

# Add button grid[1,4] colspan 2 width 36
addToFileButton = Button(text="Add", width=44, fg="white", bg="darkred", command=save)
addToFileButton.grid(column=1, row=4, columnspan=2, sticky="w")


# Goes at the end to keep the window runnung
window.mainloop()