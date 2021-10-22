# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI is weight/height squared
height = float(height)
weight = float(weight)

result = (weight / (height * height))
result = round(result, 2)

print("Your BMI is " + str(result))