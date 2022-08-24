from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_on = True

while coffee_on:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == 'off':
        coffee_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink):
            CoffeeMaker.make_coffee(drink)



