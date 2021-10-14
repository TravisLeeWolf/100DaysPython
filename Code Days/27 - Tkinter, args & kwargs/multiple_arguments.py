def add(*args): # args creates a tuple of arguments with no keyword
    sum = 0
    for number in args:
        sum += number
    return sum

# print(add(5, 10, 15))

def calculate(n, **kwargs): # kwargs creates a dictionary of values with key, value pairs
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# print(calculate(5, add=5, multiply=5))

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"] # In this case if model isn't added it will throw and error
        self.model = kwargs.get("model") # In this case it will reutrn none if there are no arguments passed

myCar = Car(make="Nissan")
print(myCar.make)
print(myCar.model)
