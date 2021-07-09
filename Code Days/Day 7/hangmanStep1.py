#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
""" Can also use this method (simpler) for below
chosen_word = random.choice(word_list)
"""
chosen_word = word_list[random.randint(0, (len(word_list) -1))]
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input("Guess a letter: ")).lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
""" Can also use this method (simpler) for below
for letter in chosen_word:
    if letter == guess:
        #do stuff
"""
for i in range(len(chosen_word) - 1):
    if guess == chosen_word[i]:
        print(True)
    else:
        print(False)
