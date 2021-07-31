import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

natoAlphabetData = pandas.read_csv("nato_phonetic_alphabet.csv")
natoAlphabetDictionary = {row.letter:row.code for (index, row) in natoAlphabetData.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userWord = input("Enter a word: ")
newNatoWord  = [natoAlphabetDictionary[letters.upper()] for letters in userWord]

print(newNatoWord)

