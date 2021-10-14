from tkinter import *
from tkinter.messagebox import askokcancel, showwarning
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Editied from Password Generator Project
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordLetterList = [choice(letters) for _ in range(randint(8, 10))]
    passwordSymbolList = [choice(symbols) for _ in range(randint(2, 4))]
    passwordNumberList = [choice(numbers) for _ in range(randint(2, 4))]

    passwordList = passwordLetterList + passwordSymbolList + passwordNumberList

    shuffle(passwordList)

    password = "".join(passwordList)

    passwordInput.delete(0, END)
    passwordInput.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websiteText = websiteInput.get()
    emailUsernameText = emailUsernameInput.get()
    passwordText = passwordInput.get()
    newDataEntry = {
        websiteText:{
            "email":emailUsernameText,
            "password":passwordText
        }
    }

    if websiteText == "" or passwordText == "":
        showwarning(title="Missing Fields!", message="Please enter in all fields.")
    else:
        try:
            with open("data.json", mode="r") as dataFile:
                data = json.load(dataFile)
                data.update(newDataEntry)
        except FileNotFoundError:
            with open("data.json", mode="w") as dataFile:
                json.dump(newDataEntry, dataFile, indent=4)
        else:
            with open("data.json", mode="w") as dataFile:
                json.dump(data, dataFile, indent=4)
        finally:
            websiteInput.delete(0, END)
            passwordInput.delete(0, END)


# ------------------------- SEARCH FUNCTION ---------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as dataFile:
            data = json.load(dataFile) 
    except FileNotFoundError:
        print("There are no entries, please save an entry first.")
    else:
        try:
            websiteToSearch = websiteInput.get()
            resultEntry = data[websiteToSearch]
            print(resultEntry)
        except KeyError:
            askokcancel(title="Not Found", message=f"{websiteToSearch} does not exist in the database.")
        else:
            askokcancel(title="Search Result", message=f"Details for {websiteToSearch}:\nEmail: {resultEntry['email']}\nPassword: {resultEntry['password']}")
    finally:
        websiteInput.delete(0, END)
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
websiteInput = Entry(width=32)
websiteInput.grid(column=1, row=1, sticky="w")
websiteInput.focus()

# Search button grid[1,2]
searchButton = Button(text="Search", fg="white", bg="darkred", width=15, command=find_password)
searchButton.grid(column=2, row=1, sticky="w")

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
passwordInput = Entry(window, width=32, show="*")
passwordInput.grid(column=1, row=3, sticky="w")

# Generate Password button grid[2,3]
generatePasswordButton = Button(text="Generate Password", fg="white", bg="darkred", width=15, command=generatePassword)
generatePasswordButton.grid(column=2, row=3, sticky="w")

# Add button grid[1,4] colspan 2 width 36
addToFileButton = Button(text="Add", width=44, fg="white", bg="darkred", command=save)
addToFileButton.grid(column=1, row=4, columnspan=2, sticky="w")


# Goes at the end to keep the window runnung
window.mainloop()