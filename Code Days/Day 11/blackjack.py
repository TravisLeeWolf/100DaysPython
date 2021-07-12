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

# Select 2 cards for player
for _ in range(2):
    pick_a_card(players_hand)
    pick_a_card(dealers_hand)
print(f"Your cards: {players_hand}")
# Select 2 cards for dealer, only one card is shown
print(f"Dealer's first card: {dealers_hand[0]}")

# Ask player to hit (take another card) or stand (show dealers hand)
another_card = input("Type 'y' to get another card, type 'n' to pass: ")
if another_card == "y":
    pick_a_card(players_hand)
    print(f"Your cards: {players_hand}")
# TODO - Player can take multiple hits until bust
    
# Evaluate both player and dealers hands
player_score = 0
for card in players_hand:
    player_score += card
print(f"Final score: {player_score}")

dealer_score = 0
for card in dealers_hand:
    dealer_score += card
print(f"Dealer's score: {dealer_score}")
# The dealer does not hit until all players have either busted, stayed or received blackjack.
#TODO Dealer hits if card score is less than 17

# If either is over 21 the other wins
# If both player and dealer are below 21, evaluate which is closest to 21
if player_score > 21:
    print("You went over. You lose 😭")
elif dealer_score > 21:
    print("Dealer went over. You win! 🤑")
elif player_score == dealer_score:
    print("It's a draw 😑")
elif player_score > dealer_score:
    print("You win! 🤑")
else:
    print("You lose. 😭")

# Ask if the player wants to play again
keep_playing = True
play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while keep_playing == True:
    if play_again == "y":
        pass
        # Clear the player and dealers hands
        players_hand = []
        dealers_hand = []
        # Play game again
    else:
        keep_playing = False