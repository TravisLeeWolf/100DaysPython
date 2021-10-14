import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameHands = [rock, paper, scissors]

print("Type '0' for rock, '1' for paper or '2' for scissors.")
userChoice = int(input("What do you choose?\n"))

print()
print("You chose:")
print(gameHands[userChoice])

computerChoice = random.randint(0,2)
print("Computer chose:")
print(gameHands[computerChoice])

# Rock beats scissors
# Paper beats rock
# Scissors beats paper

winScenario = ["02","10","21"]
loseScenario = ["20", "01", "12"]

outcomeText = str(userChoice) + str(computerChoice)


if outcomeText in winScenario:
    print("You win!")
elif outcomeText in loseScenario:
    print("You lose!")
else:
    print("Draw!")
