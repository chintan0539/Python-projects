from menu import Menu
from coffee_maker import CoffeeMaker

from money_machine import MoneyMachine

m = CoffeeMaker()
menu = Menu()

mm = MoneyMachine()

flag = True
while flag:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        flag = False
    elif choice == "report":
        print(m.report())
    else:
        drink_present = menu.find_drink(choice)
        drink = menu.find_drink(choice)
        print(drink)
        if drink_present:
            res_present = m.is_resource_sufficient(drink)
            if res_present:
                enough_payment = mm.make_payment(drink.cost)
                if enough_payment:
                    m.make_coffee(drink)