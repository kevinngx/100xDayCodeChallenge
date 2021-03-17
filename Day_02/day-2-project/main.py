#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
num_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?")) / 100

split_amount = round((total * (1+tip_percentage)) / num_people, 2)

print(f"${split_amount}")