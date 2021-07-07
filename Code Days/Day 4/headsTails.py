#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

print("Coin flipped, it's...")

coinFlip = random.randint(1, 2)

if coinFlip == 1:
    print("Heads")
elif coinFlip == 2:
    print("Tails")
