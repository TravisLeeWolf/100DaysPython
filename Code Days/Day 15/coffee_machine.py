from coffee_machine_data import menu, resources
"""
Program requirements
1. Print report
2. Check if resources are sufficient
3. Process coins
4. Check if the transaction was successful
5. Make coffee
"""
WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0

# Coin values
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

# Print report
def report():
    """Prints out the current value in the machine of water, milk, coffee and money."""
    return f"Water: {WATER}ml\nMilk: {MILK}ml\nCoffee: {COFFEE}g\nMoney: ${MONEY}"

# Take order
def get_order():
    """Gets order from the customer and returns that order."""
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print(report())
    elif order not in ["espresso", "latte", "cappuccino"]:
        print("This machine doesn't offer that, sorry.")
    else:
        return order

# Check if resources are sufficient
def check_resources(order):
    """Checks if there are enough resources in machine, returns True if there is and False if not."""
    drink = resources[order]["ingredients"]
    if order == "espresso":
        if WATER < drink["water"] or COFFEE < drink["coffee"]:
            return False
    else:
        if WATER < drink["water"] or MILK < drink["milk"] or COFFEE < drink["coffee"]:
            return False
    return True

def get_money():
    """Gets payment from customer and returns the amount of money they put in."""
    money_in = 0.0
    pennies = PENNY * int(input("How many pennies? "))
    nickels = NICKEL * int(input("How many nickels? "))
    dimes = DIME * int(input("How many dimes? "))
    quaters = QUARTER * int(input("How many quaters? "))
    money_in = pennies + nickels + dimes + quaters
    return money_in


# Process
def process_payment(order, resources_available):
    """Takes the order and if there are resources available, if resources are available then processes order and returns change."""
    if resources_available:
        drink_cost = resources[order]["cost"]
        print(f"The cost for a {order} is ${drink_cost: .2f}.")
        payment = get_money()
        if drink_cost < payment:
            MONEY += drink_cost
            change = payment - drink_cost
            return change
        else:
            print("Not enough coins, sorry.")
            return False
    else:
        print("Not enough ingredients, sorry.")
        return False

