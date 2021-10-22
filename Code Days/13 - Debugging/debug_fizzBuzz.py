for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #NOTE: changed or to and
    print("FizzBuzz")
  elif number % 3 == 0: #NOTE: changed if statements to elif statements
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)