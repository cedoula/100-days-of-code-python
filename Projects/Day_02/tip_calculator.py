#Welcome message
print("Welcome to the Tip Calculator.")
#Gather inputs from the user
bill = float(input("What was the total bill? $"))
tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
#Calculate payment per person and use "{:.2f}".format() to round at 2 decimal places
payment = "{:.2f}".format((bill * (1 + tip_perc / 100)) / people)
#Print amount to pay per person
print(f'Each person should pay: ${payment}')