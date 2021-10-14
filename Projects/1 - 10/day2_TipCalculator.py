#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Tired of having to workout the bill at the end of a meal?\nTry this tip calculator!")
bill = int(input("What's the bill total? "))
split = int(input("How many people is it going to be split by? "))
tip = int(input("What's the tip in %: "))

perPersonTotal = (bill / split) * (1 + (tip / 100))

print(f"The bill is ${bill:.2f} that's split by {split} people with a tip of {tip}%")
print(f"You each need to pay ${perPersonTotal:.2f}.")