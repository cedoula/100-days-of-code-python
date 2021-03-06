from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Operations dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  continue_calc = True
  while continue_calc:
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    decision = input(f"Type 'y' to continue calculation with {answer}, or type 's' to start a new calculation, or type 'n' to exit: ")

    if decision == 'y':
      num1 = answer
    else:
      continue_calc = False
      if decision == 's':
        calculator()

calculator()