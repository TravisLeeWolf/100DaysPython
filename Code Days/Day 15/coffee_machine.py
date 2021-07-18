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

# Print report
def report():
    return f"Water: {WATER}ml\nMilk: {MILK}ml\nCoffee: {COFFEE}g\nMoney: ${MONEY}"

# Take order
order = input("What would you like? (espresso/latte/cappuccino): ")
if order == "report":
    print(report())
elif order not in ["espresso", "latte", "cappuccino"]:
    print("This machine doesn't offer that, sorry.")

item = menu[order]["ingredients"]
item_cost = menu[order]["cost"]

print(item)

# Check if resources are sufficient

# Process 