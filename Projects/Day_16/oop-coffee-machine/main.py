from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
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


#Create instances of coffee and money machines and a menu
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

clear()
print(logo)

turn_off = False
while not turn_off:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "off":
        turn_off = True
    elif user_choice == "report":
        coffee_maker.report()  
        money_machine.report()
    else:
        item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)