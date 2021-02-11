MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

while True:
    menu_name = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 1. Print report of all coffee machine resources
    if menu_name == "report":
        print(f"Water: {resources.get('water')}ml")
        print(f"Milk: {resources.get('milk')}ml")
        print(f"Coffee: {resources.get('coffee')}g")
        print(f"Money: ${resources.get('money')}")
        continue

    if menu_name in ['espresso', 'latte', 'cappuccino']:
        menu = MENU[menu_name]
        # TODO: 2. Check resources sufficient to make drink order.
        is_sufficient_ingredients = True
        is_not_sufficient_ingredient = ""

        for key, value in menu["ingredients"].items():
            if resources[key] < value:
                is_sufficient_ingredients = False
                is_not_sufficient_ingredient = key
                break

        if not is_sufficient_ingredients:
            print(f"Sorry there is not enough {is_not_sufficient_ingredient}.")
            continue

        # TODO: 3. insert coins and check money enough
        print("Please insert coins.")
        total_coins = 0
        total_coins += int(input("How many quarters?: ")) * 0.25
        total_coins += int(input("How many dimes?: ")) * 0.1
        total_coins += int(input("How many nickles?: ")) * 0.05
        total_coins += int(input("How many pennies?: ")) * 0.01

        menu_cost = menu["cost"]
        is_enough_money = total_coins >= menu_cost

        if not is_enough_money:
            print("Sorry there is not enough money. Money refunded.")
            continue

        # TODO: 4. give change and serve menu
        resources['money'] += menu_cost
        print(f"Here is ${total_coins - menu_cost} in change.")

        for key, value in menu["ingredients"].items():
            resources[key] -= value

        print(f"Here is your ${menu_name} ☕ Enjoy!")

