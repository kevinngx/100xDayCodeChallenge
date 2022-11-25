import random



# 1. Introductions and Preparation
print("*************************************")
print("Welcome to the Number Guessing Game!")
print("*************************************\n")

print("I'm thinking of a number between 1 and 100")
number = random.randint(0,100)
print(f"Shh the number is {number}\n")

# 2. Set difficulty
difficulty = input("Choose a difficulty 'easy' or 'hard' ")

attempts = 0
if (difficulty == "hard"):
  attempts = 5
elif (difficulty == "easy"):
  attempts = 10

#3. Start guessing

correct_guess = False
while (attempts > 0) and (correct_guess == False):
  print(f"\nYou have {attempts} remaining to guess the number")
  attempts -= 1
  guess = int(input("Make a guess: "))
  if (guess == number):
    correct_guess = True
  elif (guess > number):
    print("Too high.")
  elif (guess < number):
    print("Too low.")

# 4. Print result

if (correct_guess == True):
  print("\nCongratulations, you have correctly guessed the number!")
else:
  print("\nSorry, the number was actually {number}")