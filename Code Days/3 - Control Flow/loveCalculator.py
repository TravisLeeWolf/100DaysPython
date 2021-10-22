# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# Use the lower() and count() functions
bothNames = (name1 + name2).lower()
trueTotal = 0
loveTotal = 0

if bothNames.count("t") > 0 or bothNames.count("r") > 0 or bothNames.count("u") > 0 or bothNames.count("e") > 0:
    trueTotal = bothNames.count("t") + bothNames.count("r") + bothNames.count("u") + bothNames.count("e")

if bothNames.count("l") > 0 or bothNames.count("o") > 0 or bothNames.count("v") > 0 or bothNames.count("e") > 0:
    loveTotal = bothNames.count("l") + bothNames.count("o") + bothNames.count("v") + bothNames.count("e")

match = int(str(trueTotal)+str(loveTotal))

if match < 10 or match > 90:
    print(f"Your score is {match}, you go together like coke and mentos.")
elif match >= 40 and match <= 50:
    print(f"Your score is {match}, you are alright together.")
else:
    print(f"Your score is {match}.")