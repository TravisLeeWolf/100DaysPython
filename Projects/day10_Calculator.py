import day10_CalculatorArt

# Functions

# Add
def add(a, b):
    """Returns the addition of two numbers"""
    answer = a + b
    return answer

# Subtract
def subtract(a, b):
    """Returns the subtraction of two numbers"""
    answer = a - b
    return answer

# Multiply
def multiply(a, b):
    """Returns the multiplication of two numbers"""
    answer = a * b
    return answer

# Divide
def divide(a, b):
    """Returns the division of two numbers"""
    if b != 0:
        answer = a / b
        return answer
    else:
        print("Can't divide by 0!")

# Get numbers and operation
def get_numbers_and_operation():
    """Gets the number input and operator to use, first number then operation and last number"""
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    last_number = float(input("What's the next number?: "))

    print(f"{first_number} {operation} {last_number} = ")
    return first_number, operation, last_number

# Perform calculation using numbers and operation
def perform_calculation(first_number, operation, last_number):
    """Takes the numbers provided and operator and assigns which calculation to perform"""
    if operation == "+":
        add(first_number, last_number)
    elif operation == "-":
        subtract(first_number, last_number)
    elif operation == "*":
        multiply(first_number, last_number)
    elif operation == "/":
        divide(first_number, last_number)
    else:
        print("An error ocurred.")

# Start here
print(day10_CalculatorArt.logo)

# First run
first_number, operation, second_number = get_numbers_and_operation()
print(perform_calculation(first_number, operation, second_number))