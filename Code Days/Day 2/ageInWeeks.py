# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 365 days, 52 weeks, 12 months
# Take 90 (assumption if you'd live till 90 years old) minus the age

# Use f-strings for the output
age = int(age)
yearsLeft = 90 - age
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"You have {monthsLeft} months left, {weeksLeft} weeks left and {daysLeft} days left.")
print("Make them count!")