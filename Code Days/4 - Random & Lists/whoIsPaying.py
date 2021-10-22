# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

picker = random.randint(0, (len(names) - 1))
personPaying = names[picker]
# Below is a much easier solution
#personPaying = random.choice(names)

print(f"{personPaying} is going to buy the meal today!")