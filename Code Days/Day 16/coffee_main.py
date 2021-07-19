from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_order = input("What would you like to order? 'latte', 'espresso' or 'cappuccino': ")
drink_from_menu = Menu()

my_drink = drink_from_menu.find_drink(my_order)

coffee_machine = CoffeeMaker()
payment_machine = MoneyMachine()

if coffee_machine.is_resource_sufficient(my_drink):
    if payment_machine.make_payment(my_drink.cost):
        coffee_machine.make_coffee(my_drink)
    else:
        print("Not enough money, sorry.")
else:
    print("Out of ingredients, sorry.")