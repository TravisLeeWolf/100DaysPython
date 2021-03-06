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
from os import system

# NOTE: Structure of data, list of dictionaries, length of list is 50 (index 49)
# data[int]['key']
# Keys - 'name', 'follower_count', 'description', 'country'

# NOTE: Display layout, logo, current score, option A, vs logo, option B, input for which option player chooses

# TODO: If the answer is correct display 'You're right!'
# TODO: Display the current score

# TODO: Get and display the options
# Layout A - Compare A: name, job , origin
# Layout B - Against B: name, job, origin

# Set up a list for current items
CURRENT_OPTIONS = []
CHOICES_LIST = []
SCORE = 0

# Clear screen to for next options to guess
def screen_clear():
    """Clears the screen."""
    system('cls')

# Get length of data and make list of the index, this list will be where you remove items already guessed
def set_options_list():
    "This function can only be run once per game, sets up a list of index from the length of data to be destructable as game progresses."
    for i in range(0, len(data)):
        CHOICES_LIST.append(i)
    return CHOICES_LIST

# Get a random option
# choice = random.randint(0, 49)
def get_option_details(data_num):
    """Given an int from 0-49, function will return the name, description and country from a list of people/brands."""
    name = data[data_num]['name']
    desc = data[data_num]['description']
    country = data[data_num]['country']
    return name, desc, country

def get_option_followers(data_num):
    """Given an int from 0-49, function will return the follower count from a list of people/brands."""
    count = data[data_num]['follower_count']
    return count

# TODO: Once chosen, remove from chosen list
def remove_from_list(data_num):
    """Take the list, number of the option chosen and removes it from the list."""
    if data_num in CHOICES_LIST:
        CHOICES_LIST.remove(data_num)

# TODO: Get input for player option choice
# Should work for upper/lower case
def get_player_choice():
    """Gets and returns the players choice between A or B."""
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if player_choice == "a":
        return True
    elif player_choice == "b":
        return False
    else:
        print("Invalid choice! Please try again.")
        get_player_choice()

# TODO: Compare both options, find which is higher
def A_higher(choiceA_num, choiceB_num):
    """Compares the followers of both options, if A is higher returns True, if B is higher returns False."""
    if get_option_followers(choiceA_num) > get_option_followers(choiceB_num):
        return True
    elif get_option_followers(choiceA_num) < get_option_followers(choiceB_num):
        return False

# TODO: Compare higher option against player choice
def compare_to_choice(choiceA_num, choiceB_num):
    """Compares the highest follower count from option A and B to the players decision, returns True if player is correct, False if player incorrect."""
    if get_player_choice() == A_higher(choiceA_num, choiceB_num):
        return True
    else:
        return False

def pick_random_item():
    """Picks a random item in CHOICES_LIST and returns the number."""
    if len(CHOICES_LIST) > 0:
        choice = random.choice(CHOICES_LIST)
        remove_from_list(choice)
    else:
        print("No more options to chose from.")
    return choice

# Choose an item from the choice list and display it
def display_option(choice_num):
    """Given the random item number, returns the details of the choice."""
    name, desc, country = get_option_details(choice_num)
    option_description = f"{name}, a {desc}, from {country}."
    return option_description

def show_options_get_choice():
    """Displays the options and asks the user for a guess."""
    option_a = display_option(CURRENT_OPTIONS[0])
    option_b = display_option(CURRENT_OPTIONS[1])
    screen_clear()
    print(art.logo)
    if SCORE > 0:
        print(f"You're right! Current score: {SCORE}")
    print("Compare A: " + option_a)
    print(art.vs)
    print("Against B: " + option_b)
    check_options_assign_new()

# TODO: If incorrect, display final score and end game
def end_game():
    """If user gets the answer wrong, end the game."""
    screen_clear()
    print(f"Sorry, that's wrong. Final score: {SCORE}")

# TODO: If correct, move option B up to A and select a new option B
def check_options_assign_new():
    """Checks if the guess is correct, if True then keep going, else end the game."""
    if compare_to_choice(CURRENT_OPTIONS[0], CURRENT_OPTIONS[1]):
        CURRENT_OPTIONS[0] = CURRENT_OPTIONS[1]
        CURRENT_OPTIONS[1] = pick_random_item()
        # Add 1 to score
        global SCORE
        SCORE += 1
        # Start next guess with new choices
        show_options_get_choice()
    else:
        end_game()

# TODO: Start the game with two choices, remove them from the choice list.
set_options_list()
for i in range(2):
    CURRENT_OPTIONS.append(pick_random_item())
show_options_get_choice()