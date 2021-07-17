# Made by TravisLeeWolf

# NOTE - About the game
"""
In this game you will be given two options, from them you decide which person/brand has more followers.
The information the player gets is, the name of the person/brand, their job and where they're from.
Starting out you have two random selections, after that the bottom person/brand is moved up
and compared to the next person/brand like a line moving one by one.
The point of the game is that you get a point for consecutively answering correctly, 
if you get one answer wrong the game ends.
"""
from game_data import data
import art
import random

# NOTE: Structure of data, list of dictionaries, length of list is 50 (index 49)
# data[int]['key']
# Keys - 'name', 'follower_count', 'description', 'country'

# NOTE: Display layout, logo, current score, option A, vs logo, option B, input for which option player chooses

# TODO: If the answer is correct display 'You're right!'
# TODO: Display the current score

# TODO: Get and display the options
# Layout A - Compare A: name, job , origin
# Layout B - Against B: name, job, origin

# Get a random option
# choice = random.randint(0, 49)
def get_option_details(data_num):
    """Given an int from 0-49, function will return the name, description and country from a list of people/brands."""
    name = data[data_num]['name']
    desc = data[data_num]['description']
    country = data[data_num]['country']
    return name, desc, country
# name, desc, country = get_option(choice)
# print(f"{name}, a {desc}, from {country}.")

def get_option_followers(data_num):
    """Given an int from 0-49, function will return the follower count from a list of people/brands."""
    count = data[data_num]['follower_count']
    return count

# TODO: Get input for player option choice
# Should work for upper/lower case
def get_player_choice():
    """Gets and returns the players choice between A or B."""
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if player_choice == "a":
        return "a"
    elif player_choice == "b":
        return "b"
    else:
        print("Invalid choice! Please try again.")
        get_player_choice()

# TODO: Compare both options, find which is higher
optionA = random.randint(0, 49)
optionB = random.randint(0, 49)
if get_option_followers(optionA) > get_option_followers(optionB):
    print("Option A is higher")
    print(get_option_details(optionA), get_option_details(optionB))
elif get_option_followers(optionA) < get_option_followers(optionB):
    print("Option B is higher")
    print(get_option_details(optionA), get_option_details(optionB))
else:
    print("It's the same.")
    print(get_option_details(optionA), get_option_details(optionB))
# TODO: Compare higher option against player choice

# TODO: If correct, move option B up to A and select a new option B

# TODO: If incorrect, display final score and end game