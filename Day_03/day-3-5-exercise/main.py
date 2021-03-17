# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
fullName = name1 + name2
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Count True
trueCount = 0
trueCount += fullName.count('t') + fullName.count('r') + fullName.count('u') + fullName.count('e')

#Count Love
loveCount = 0
loveCount += fullName.count('l') + fullName.count('o') + fullName.count('v') + fullName.count('e')

loveScore = int(str(trueCount) + str(loveCount))

if (loveScore < 10 or loveScore > 90):
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore < 40 or loveScore > 50):
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}")
