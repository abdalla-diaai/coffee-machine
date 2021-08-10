from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while is_on:
    choice = input("What would you like to drink (latte/espresso/cappuccino)?\n").lower()
    if choice == "report":
        coffee.report()
    elif choice == "OFF":
        is_on = False
    elif choice in menu.get_items():
        chosen_drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(chosen_drink):
            print(f"{chosen_drink.name} cost ${chosen_drink.cost}.")
            if money.make_payment(chosen_drink.cost):
                coffee.make_coffee(chosen_drink)
        else:
            is_on = False
    else:
        print(f"{choice} is not available!")
        is_on = False





