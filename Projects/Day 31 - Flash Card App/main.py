# Created by @travisleewolf, started 2021/07/05, finished 

# Project imports
from tkinter import *
import pandas
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"

# Globals
chosenWord = {}
wordsToLearn = []


wordDataDF = pandas.read_csv(".\data\\french_words.csv")
wordDictionaryList = wordDataDF.to_dict(orient="records")


# --- Check which data file to use --- #
# If words_to_learn.cv exists, use that file, else start from here
def loadDataToUse():
    global wordsToLearn
    try:
        savedData = pandas.read_csv(".\data\words_to_learn.csv")
    except FileNotFoundError:
        wordsToLearn = wordDictionaryList
    else:
        wordsToLearn = savedData.to_dict(orient="records")


# --- Switch to English --- #
def flipCardToEnglish():
    global chosenWord
    cardCanvas.itemconfig(cardImage, image=cardBack)
    languageOfCard.config(text="English", bg=CARD_BACK_COLOR, fg="white")
    wordOfCard.config(text=chosenWord["English"], bg=CARD_BACK_COLOR, fg="white")   


# --- Create New Flash Card --- #
def createNewFlashCard():
    global chosenWord, cardTimer
    window.after_cancel(cardTimer)
    cardCanvas.itemconfig(cardImage, image=cardFront)
    chosenWord = choice(wordsToLearn)
    languageOfCard.config(text="French", bg="white", fg="black")
    wordOfCard.config(text=chosenWord["French"], bg="white", fg="black")
    cardTimer = window.after(3000, flipCardToEnglish)

# --- Save current list of remaining words to learn --- #
def saveToWordsToLearn():
    listAsDF = pandas.DataFrame(wordsToLearn)
    listAsDF.to_csv(".\data\words_to_learn.csv", index=False)

# --- Remove learnt word from words_to_learn.csv --- #
def removeFromLearningList():
    wordsToLearn.remove(chosenWord)
    saveToWordsToLearn()
    createNewFlashCard()


# --- UI --- #
window =Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

cardTimer = window.after(3000, flipCardToEnglish) # NOTE: Find a way to implement this better, needs to exist or createNewFlashCard with throw an error

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
rightGuessButton = Button(image=rightImage, bg=BACKGROUND_COLOR, highlightthickness=0, relief=FLAT, command=removeFromLearningList)
rightGuessButton.grid(column=1, row=1)

# Starting function calls
loadDataToUse()
createNewFlashCard()

# Keeps the window open
window.mainloop()