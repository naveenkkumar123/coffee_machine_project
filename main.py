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
}

def check_ingredients(ingredients):
    """checking the ingredints"""
    global resources
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True

def calculate_bill():
    amount = 0
    amount += int(input("Please insert coins of quarters: ")) * 0.25
    amount += int(input("Please insert coins of dimes: ")) * 0.10
    amount += int(input("Please insert coins of nickels: ")) * 0.05
    amount += int(input("Please insert coins of quarters: ")) * 0.01
    return round(amount,2)


def deduct_resources(ingredients):
    """deduct the resources"""
    global resources
    for item in ingredients:
        resources[item] -= ingredients[item]





profit = 0
is_on = True
while is_on :
    order = input("what would you Like?: ")
    if order == "off":
        is_on = False

    elif order == "report":
        #
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}")
        print(f"coffee_powder:{resources['coffee']}")

    else:
        drink = MENU[order]
        if check_ingredients(drink["ingredients"]):
            amount = calculate_bill()
            if amount < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += drink["cost"]
                print(f"Enjoy Your {order} coffee ☕")
                deduct_resources(drink["ingredients"])
                change = amount - drink["cost"]
                print(f"Keep the $change : {round(change,2)}")





