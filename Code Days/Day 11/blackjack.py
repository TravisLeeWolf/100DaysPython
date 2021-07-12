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

# Logo for the game
print(logo)

# List of cards used to play the game
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Select 2 cards for player

# Select 2 cards for dealer, only one card is shown

# Ask player to hit (take another card) or stand (show dealers hand)

# Evaluate both player and dealers hands, if either is over 21 the other wins

# If both player and dealer are below 21, evaluate which is closest to 21

# Ask if the player wants to play again