from menu_del import MENU, resources

flag = True


def res_checker(drink):
    a = MENU[drink]["ingredients"]

    for i in a:
        if a[i] >= resources[i]:
            print("there is not enough " + i)
            return False

    return True


def coin_validate(available, choice):
    if available:
        print("Plzz, Enter coins")
        final_money: float = 0
        final_money += int(input("How many quarters: ")) * 0.25
        final_money += int(input("How many dimes: ")) * 0.10
        final_money += int(input("How many nickles: ")) * 0.05
        final_money += int(input("How many pennies: ")) * 0.01

        if final_money >= MENU[choice]["cost"]:
            change = round(final_money - MENU[choice]['cost'], 2)
            print(f"Here is your change: ${change}")
            update_resources(choice)

        else:
            print("“Sorry that's not enough money. Money refunded.")


def update_resources(choice):
    a = MENU[choice]["ingredients"]
    for i in a:
        resources[i] -= a[i]
    print(f"Here is your {choice}. Enjoy!")



while flag:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "espresso":
        are_res_available = res_checker("espresso")
    elif choice == "latte":
        are_res_available = res_checker("latte")
    elif choice == "cappuccino":
        are_res_available = res_checker("cappuccino")
    elif choice == "report":
        for r in resources:
            print(f"{r} : {resources[r]}")
    elif choice == "off":
        print("machine turned off")
        flag = False
    else:
        print("Plzz, enter correct choice")

    coin_validate(are_res_available,choice)