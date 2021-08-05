# Created by @travisleewolf, started 2021/07/05, finished 

# Project imports
from tkinter import *
import pandas
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"


# --- Switch to English --- #
def flipCardToEnglish(currentWord):
    cardCanvas.itemconfig(cardImage, image=cardBack)
    languageOfCard.config(text="English", bg=CARD_BACK_COLOR)
    wordOfCard.config(text=currentWord["English"], bg=CARD_BACK_COLOR)

    

# --- Create New Flash Card --- #
wordDataDF = pandas.read_csv(".\data\\french_words.csv")
wordDictionaryList = wordDataDF.to_dict(orient="records")
def createNewFlashCard():
    cardCanvas.itemconfig(cardImage, image=cardFront)
    chosenWord = choice(wordDictionaryList)
    languageOfCard.config(text="French", bg="white")
    wordOfCard.config(text=chosenWord["French"], bg="white")
    window.after(3000, flipCardToEnglish, chosenWord)

# --- UI --- #
window =Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# UI is broken up into a 2 X 2 grid
## Adding the flash card image
cardCanvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardFront = PhotoImage(file=".\images\card_front.png")
cardBack = PhotoImage(file=".\images\card_back.png")
cardImage = cardCanvas.create_image(400, 263, image=cardFront)
cardCanvas.grid(column=0, row=0, columnspan=2)

## Label for the language shown on the card
languageOfCard = Label(text="Language", font=("Ariel", 40, "italic"))
languageOfCard.place(x=400, y=150, anchor=CENTER)

## Label for the cards text
wordOfCard = Label(text="Word", font=("Ariel", 60, "bold"))
wordOfCard.place(x=400, y=263, anchor=CENTER)

## X button if guess was wrong
wrongImage = PhotoImage(file=".\images\wrong.png")
wrongGuessButton = Button(image=wrongImage, bg=BACKGROUND_COLOR, highlightthickness=0, relief=FLAT, command=createNewFlashCard)
wrongGuessButton.grid(column=0, row=1)

## Tick button if guess was right
rightImage = PhotoImage(file=".\images\\right.png")
rightGuessButton = Button(image=rightImage, bg=BACKGROUND_COLOR, highlightthickness=0, relief=FLAT, command=createNewFlashCard)
rightGuessButton.grid(column=1, row=1)

# Starting function calls
createNewFlashCard()

# Keeps the window open
window.mainloop()