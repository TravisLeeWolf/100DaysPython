from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drink_from_menu = Menu()
coffee_machine = CoffeeMaker()
payment_machine = MoneyMachine()

is_on = True

while is_on:
    my_order = input("What would you like to order? 'latte', 'espresso' or 'cappuccino': ")

    if my_order == "off":
        is_on = False
    elif my_order == "report":
        print(coffee_machine.report())
        print(payment_machine.report())
    else:
        my_drink = drink_from_menu.find_drink(my_order)
        if coffee_machine.is_resource_sufficient(my_drink) and payment_machine.make_payment(my_drink.cost):
            coffee_machine.make_coffee(my_drink)
    