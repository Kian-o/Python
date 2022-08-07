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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_availability(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {resources[item]}")
            return False
    return True


def process_payment(cost):
    print(f"Total: ${cost}\nPlease insert coins:")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .1
    total += int(input("How many nickles? ")) * .05
    total += int(input("How many pennies? ")) * .01
    return total


def transaction_success(paid, cost):
    if paid >= cost:
        change = round(paid - cost, 2)
        print(f"Your change is ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


coffee_on = True

while coffee_on == True:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == 'off':
        coffee_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_availability(drink['ingredients']):
            payment = process_payment(drink['cost'])
            if transaction_success(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


