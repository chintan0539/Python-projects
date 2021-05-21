from menu import Menu  # , MenuItem
from coffee_maker import CoffeeMaker

# from money_machine import MoneyMachine

m = CoffeeMaker()
menu = Menu()
flag = True
while flag:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        flag = False
    elif choice == "report":
        print(m.report())
    else:
        drink = menu.find_drink(choice)
        print(drink)
