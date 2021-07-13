############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

from art import logo
import random

# Logo for the game
print(logo)

# List of cards used to play the game
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#TODO - Find code that can be made into repeatable functions

# Player and dealer start with empty hands
players_hand = []
dealers_hand = []

# Pick a card at random
def pick_a_card(whos_hand):
    """Takes the player or dealer's hand list and adds a card to their hand."""
    whos_hand.append(cards[random.randint(0, len(cards) -1)])
    # NOTE - you can use choice()

# Counts the current score of the persons hand
def count_score(persons_hand):
    """Takes the card list in persons hand and return the score of that hand."""
    score = 0
    for card_value in persons_hand:
        score += card_value
    return score
    # NOTE - you can use sum()

def display_table():
    """Prints out the players hand and score as well as the dealer's first card."""
    print(f" 🤠 Your cards: {players_hand}, current score: {count_score(players_hand)}")
    # Select 2 cards for dealer, only one card is shown
    print(f" 🤖 Dealer's first card: {dealers_hand[0]}")

# NOTE - Sets up the game

# The dealer does not hit until all players have either busted, stayed or received blackjack.
def dealers_play():
    """After the player chooses to stand the dealer decides if they will hit or stand."""
    while count_score(dealers_hand) < 17:
        pick_a_card(dealers_hand)

def final_results():
    print(f" 🤠 Your final hand {players_hand}, final score: {count_score(players_hand)}")
    print(f" 🤖 Dealer's final hand {dealers_hand}, final score: {count_score(dealers_hand)}")

# If either is over 21 the other wins
# If both player and dealer are below 21, evaluate which is closest to 21
def declare_winner():
    players_score = count_score(players_hand)
    dealers_score = count_score(dealers_hand)
    final_results()
    if players_score > 21:
        print("You went over. You lose 😭")
    elif dealers_score > 21:
        print("Dealer went over. You win! 🤑")
    elif players_score == dealers_score:
        print("It's a draw 😑")
    elif players_score > dealers_score:
        print("You win! 🤑")
    else:
        print("You lose. 😭")

# Ask player to hit (take another card)
def take_another_card():
    while count_score(players_hand) < 22:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            pick_a_card(players_hand)
            display_table()
        elif another_card == "n":
            display_table()
            dealers_play()
            declare_winner()
            break

# Select 2 cards for player
def new_game():
    for _ in range(2):
        pick_a_card(players_hand)
        pick_a_card(dealers_hand)
    display_table()
    take_another_card()

new_game()

# Ask if the player wants to play again
keep_playing = True
print()
play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while keep_playing == True:
    if play_again == "y":
        # Clear the player and dealers hands
        players_hand = []
        dealers_hand = []
        # Play game again
        new_game()
    else:
        keep_playing = False