# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# The input variable is stored as a 'str' so we need to convert each digit to an 'int' before adding them
digit_one = int(two_digit_number[0])
digit_two = int(two_digit_number[1])

result = digit_one + digit_two

print(result)