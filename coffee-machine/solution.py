import re
from util import MENU, resources

money = 0

def show_report():
    global money

    print("Report of current resource:")
    print(f"    Water: {resources['water']}ml")
    print(f"    Milk: {resources['milk']}ml")
    print(f"    Coffee: {resources['coffee']}g")
    print(f"    Money: Rs.{money}")

def is_resources_available(required_resources):
    if resources['water'] < required_resources['water']:
        print("Required water is not available")
    elif resources['milk'] < required_resources['milk']:
        print('Required milk is not available')
    elif resources['coffee'] < required_resources['coffee']:
        print('Required coffee is not available')
    else:
        return True
    return False

def is_user_has_required_money(user_money, required_money):
    if user_money < required_money:
        return False
    elif user_money > required_money:
        print(f"Please get back your balance {user_money - required_money}")
    return True

def compute_user_total_money(user_money):
    result = 0
    result += (user_money['ones'] * 1)
    result += (user_money['twos'] * 2)
    result += (user_money['fives'] * 5)
    result += (user_money['tens'] * 10)
    result += (user_money['twenties'] * 20)

    return result

def make_coffee(user_choice, user_money):
    global money
    
    if is_resources_available(MENU[user_choice]['ingredients']):
        user_total_money = compute_user_total_money(user_money)
        if is_user_has_required_money(user_total_money, MENU[user_choice]['cost']):
            resources['water'] -= MENU[user_choice]['ingredients']['water']
            resources['milk'] -= MENU[user_choice]['ingredients']['milk']
            resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
            money += MENU[user_choice]['cost']

            print(f"Enjoy you {user_choice}☕!")

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        show_report()
    elif user_choice == "off":
        print("Machine turned off!")
        break
    elif bool(re.match('espresso|latte|cappuccino', user_choice)):
        ones = int(input('Insert one rupee coins(if any): '))
        twos = int(input('Insert two rupee coins(if any): '))
        fives = int(input('Insert five rupee coins(if any): '))
        tens = int(input('Insert ten rupee coins(if any): '))
        twenties = int(input('Insert twenty rupee coins(if any): '))

        user_money = {}
        user_money['ones'] = ones
        user_money['twos'] = twos
        user_money['fives'] = fives
        user_money['tens'] = tens
        user_money['twenties'] = twenties

        make_coffee(user_choice, user_money)


    else:
        print('Please input the correct choice')