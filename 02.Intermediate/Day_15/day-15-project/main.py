# TODO: Update this to be an object-oriented program

import math
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

def process_order(order):
  if order == "report":
    report(resources)
  elif order == "cappuccino" or order == "latte" or  order == "espresso":
    if check_resources(order) == True:
      if request_money(order) == True:
        make_coffee(order)
  else:
    print("Invalid order")

def report(resource):
  print("\nPrinting report...")
  print("Water: " + str(resource["water"]) + "ml")
  print("Milk: " + str(resource["milk"]) + "ml")
  print("Coffee: " + str(resource["coffee"]) + "g")
  

def request_money(order):
  cost = MENU[order]["cost"]
  print(f"That would be {cost}, please insert coins")
  payment = {
    "quarters" : int(input("How many quarters?: ")),
    "dimes" : int(input("dimes? ")),
    "nickles" : int(input("nickles?: ")),
    "pennies" : int(input("pennies?: "))
  }
  payment_total = calculate_payment(payment)
  print(f"you have paid {payment_total}")
  if payment_total >= cost:
    calculate_change(cost, payment_total)
    return True
  else:
    print("Insufficient payment, returning coins...\n")
    return False

def calculate_change(cost, payment):
  change = round((payment - cost) * 100)
  print(f"Dispensing {change} cents in change...")
  quarters = math.floor(change / 25)
  change = change % 25
  dimes = math.floor(change / 10)
  change = change % 10
  nickles = math.floor(change / 5)
  change = change % 5
  pennies = change
  print(f"Quarters: {quarters} \nDimes: {dimes} \nNickles: {nickles} \nPennies: {pennies}\n")

def calculate_payment(payment):
  total = 0.0
  total += payment["quarters"] * 0.25
  total += payment["dimes"] * 0.10
  total += payment["nickles"] * 0.05
  total += payment["pennies"] * 0.01
  return total

def make_coffee(order):
  # Check resources in machine --> water, milk, coffee
  order_ingredients = MENU[order]["ingredients"]

  resources["water"] -= order_ingredients["water"]
  resources["milk"] -= order_ingredients["milk"] 
  resources["coffee"] -= order_ingredients["coffee"]
  
  return True

def check_resources(order):
  # Check resources in machine --> water, milk, coffee
  order_ingredients = MENU[order]["ingredients"]
  
  if order_ingredients["water"] > resources["water"] or order_ingredients["milk"] > resources["milk"] or order_ingredients["coffee"] > resources["coffee"]:
    print("Insufficient resources, cannot make this order\n")
    return False
  
  return True

# Main Loop of the program
repeat = True
while repeat == True:
  user_order = input("What would you like? (expresso / latte / cappuccino) ").lower()
  process_order(user_order)
  if input("Would you like to add another order? (Y/N)").lower() != "y":
    repeat = False
print("Thank you for using this coffee machine")

