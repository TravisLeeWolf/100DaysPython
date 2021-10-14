import time

def speed_calc_decorator(function):
    def timer():
        startTime = time.time()
        function()
        endTime = time.time()
        timeTaken = endTime - startTime
        print(f"{function.__name__} run speed: {timeTaken}s")
    return timer

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()