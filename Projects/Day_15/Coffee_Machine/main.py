from art import logo
from coffee_data import MENU, resources
# import only system from os 
from os import system, name 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

money = float(0)
def print_report():
    """Print report of machine resources."""
    global resources
    global money
    for resource in resources:
        if resource != "coffee":
            print(f"{resource.title()}: {resources[resource]}ml")
        else:
            print(f"{resource.title()}: {resources[resource]}g")    
    print(f"Money: ${money}")

def check_resources(drink):
    """Take drink as input and check if machine has enough resources to make it."""
    global MENU
    global resources
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    if drink != "espresso" and MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def check_amount(drink, inserted):
    global money
    if inserted < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if inserted > MENU[drink]["cost"]:
            change = "{:.2f}".format(inserted - MENU[drink]["cost"])
            print(f"Here is ${change} in change.")
        money += MENU[drink]["cost"]
        return True

def update_resources(drink):
    global resources
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]

clear()
print(logo)

turn_off = False

while not turn_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        turn_off = True
    elif user_choice == "report":
        print_report()
    else:
        enough_resources = check_resources(user_choice)
        if enough_resources:
            amount_inserted = process_coins()
            transaction_successful = check_amount(user_choice, amount_inserted)
            if transaction_successful:
                update_resources(user_choice)
                print(f"Here is your {user_choice} ☕. Enjoy!")





