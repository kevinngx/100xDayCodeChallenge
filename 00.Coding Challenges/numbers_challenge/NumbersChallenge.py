import itertools

TEST_INPUT = "40 1 3 4 20"
OPERATIONS = ["+", "-", "*","+", "-", "*","+", "-", "*","+", "-", "*"]

numbers = TEST_INPUT.split(" ")

def compute(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y

def run_combination(num, ops):
    number = int(num[0])
    number = compute(number, int(num[1]), ops[0])
    number = compute(number, int(num[2]), ops[1])
    number = compute(number, int(num[3]), ops[2])
    number = compute(number, int(num[4]), ops[3])
    return number

# Main code starts here
number_permutations = itertools.permutations(numbers, len(numbers))
operation_permutations = itertools.permutations(OPERATIONS, 4)

magic_number = False
for num in number_permutations:
    print(num)
    if num == ('4', '20', '40', '3', '1'):
        print("number")
        print(num)
        for ops in operation_permutations:
            result = run_combination(num, ops)
            if  result == 42:
                magic_number = True
                print(ops)
                print(num)
    
if magic_number == True:
    print("Yes")
else:
    print("No")
