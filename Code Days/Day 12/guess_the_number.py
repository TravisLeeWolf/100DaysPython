# Created by TravisLeeWolf
# 2021 / 07 / 14
# 100 Days of Code - Day 12

logo = """

 e88~~\                                            ,d         ,d   ,88~~\     ,88~~\   
d888     888  888  e88~~8e   d88~\  d88~\       ,d888      ,d888  d888   \   d888   \  
8888 __  888  888 d888  88b C888   C888           888 ____   888 88888    | 88888    | 
8888   | 888  888 8888__888  Y88b   Y88b          888        888 88888    | 88888    | 
Y888   | 888  888 Y888    ,   888D   888D         888        888  Y888   /   Y888   /  
 "88__/  "88_-888  "88___/  \_88P  \_88P          888        888   `88__/     `88__/   
                                                                                       
"""

from random import randint

# TODO - Greet the user at the begining of the game
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# TODO - Pick a random number from 1 - 100
answer = randint(1,100)

# TODO - Prompt the user for difficulty, easy 10 attempts, hard 5 attempts
attempts = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

# TODO - Loop for user to make a guess until correct or attempts are over
while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess == answer:
        print("That's right!")
        break
    else:
        # TODO - Remove attempt if incorrect guess
        attempts -= 1
        print(f"You have {attempts} attempts left.")
        # TODO - Let user know if guess is too high or too low
        if guess > answer:
            print("Too high.")
        elif guess < answer:
            print("Too low.")
if attempts == 0:
    print(f"Unlucky, the number was {answer}.")
