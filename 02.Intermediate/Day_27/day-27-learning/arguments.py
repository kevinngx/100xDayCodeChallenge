def add_all (*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add_all(1, 2, 3, 4, 5, 6))
# print(add_all(3, 5, 6))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(8, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Honda", model="Civic", color="Hello")
print(my_car)