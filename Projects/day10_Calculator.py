import day10_CalculatorArt

# Functions

# Add
def add(a, b):
    """Returns the addition of two numbers"""
    return a + b

# Subtract
def subtract(a, b):
    """Returns the subtraction of two numbers"""
    return a - b

# Multiply
def multiply(a, b):
    """Returns the multiplication of two numbers"""
    return a * b

# Divide
def divide(a, b):
    """Returns the division of two numbers"""
    if b != 0:
        return a / b
    else:
        print("Can't divide by 0!")

# Dictionary of operations and their function names
operators = {"+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide}

# Get numbers and operation
def get_numbers_and_operation():
    """Gets the number input and operator to use, first number then operation and last number"""
    first_number = float(input("What's the first number?: "))
    for symbol in operators:
        print(symbol)
    operation = input("Pick an operation: ")
    last_number = float(input("What's the next number?: "))
    
    # Perform calculation
    answer = operators[operation](first_number, last_number)
    
    return f"{first_number} {operation} {last_number} = {answer}"


# Start here
print(day10_CalculatorArt.logo)

# First run
print(get_numbers_and_operation())