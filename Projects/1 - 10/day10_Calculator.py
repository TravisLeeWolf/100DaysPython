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
operators = {
            "+" : add,
            "-" : subtract,
            "x" : multiply,
            "/" : divide
            }

print(day10_CalculatorArt.logo)

def calculator():
    # Get numbers and operation
    first_number = float(input("What's the first number?: ")) 
    for symbol in operators:
        print(symbol)

    continue_calculation = True

    while continue_calculation == True:
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
                
        # Perform first calculation
        answer = operators[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")

        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if keep_going == "y":
            first_number = answer
        else:
            continue_calculation = False
            calculator()

calculator()