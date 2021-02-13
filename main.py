from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money_coffer = MoneyMachine()

is_on = True

while is_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ")

    if user_input == "report":
        coffee_machine.report()
    elif user_input == "espresso":
        espresso = menu.find_drink('espresso')
        if coffee_machine.is_resource_sufficient(espresso):

            if money_coffer.make_payment(espresso.cost):
                coffee_machine.make_coffee(espresso)

    elif user_input == "latte":
        latte = menu.find_drink('latte')
        if coffee_machine.is_resource_sufficient(latte):

            if money_coffer.make_payment(latte.cost):
                coffee_machine.make_coffee(latte)

    elif user_input == "cappuccino":
        cappuccino = menu.find_drink('cappuccino')
        if coffee_machine.is_resource_sufficient(cappuccino):

            if money_coffer.make_payment(cappuccino.cost):
                coffee_machine.make_coffee(cappuccino)
    elif user_input == "off":
        is_on = False
