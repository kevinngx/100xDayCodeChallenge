import art
print(art.logo)

def add(a, b):
  return a + b

def deduct(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def calculate(a, b, operation):
  if operation == "+" :
    return add(a, b)
  elif operation == "-" :
    return deduct(a, b)
  elif operation == "*" :
    return multiply(a, b)
  elif operation == "/" :
    return divide(a, b)
  else: 
    print("Invalid operator")

# Get User Input
a = int(input("What's the first number?: "))

repeat = "y"
while repeat == "y":

  # Get input for second number
  print("+\n-\n*\n/")
  operator = input("Pick an operation: ")
  b = int(input("What's the next number?: "))


  # Perform Calculation
  result = calculate(a, b, operator)
  print(f"{a} {operator} {b} = {result}")

  # Repetition
  repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to end the program").lower()
  a = result

print(f"Calculations completed, final result = {result}")