# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI weight / height squared

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(height)
weight = float(weight)

result = (weight / (height * height))

if result < 18.5:
    print(f"Your BMI is {result:.2f} you are underweight.")
elif result >= 18.5 and result < 25:
    print(f"Your BMI is {result:.2f} you have a normal weight.")
elif result >= 25 and result < 30:
    print(f"Your BMI is {result:.2f} you are slightly overweight.")
elif result >= 30 and result < 35:
    print(f"Your BMI is {result:.2f} you are obese.")
elif result >= 35:
    print(f"Your BMI is {result:.2f} you are clinically obese.")
else:
    print("You must be an alien!")