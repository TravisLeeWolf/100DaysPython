def logginingDecorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper

@logginingDecorator
def addThreeNumbers(a, b, c):
    sum = a + b + c
    return sum

addThreeNumbers(1, 2, 3)