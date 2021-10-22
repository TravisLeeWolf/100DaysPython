height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.\nSorry if you're actually that tall.")

bmi = weight / height ** 2
print(f"Your BMI is: {bmi}")