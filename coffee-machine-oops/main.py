from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import re

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        coffeeMaker.report()
    elif user_choice == "off":
        print("Machine turned off!")
        break
    elif bool(re.match('espresso|latte|cappuccino', user_choice)):
        coffeeDetails = menu.find_drink(user_choice)
        if coffeeDetails != None:
            if coffeeMaker.is_resource_sufficient(coffeeDetails):
                if moneyMachine.make_payment(coffeeDetails.cost):
                    coffeeMaker.make_coffee(coffeeDetails)
    else:
        print('Please input the correct choice')