############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21): #NOTE: The range(1, 20) function starts from 1 and stops at 19, changed to range(1, 21)
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #NOTE: The indexes are from [0-5]
# dice_num = randint(1, 6) - 1 #NOTE: With randint(1,6) IndexError: list index out of range, changed to randint(1,6) - 1
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1978 and year <= 1995:         #NOTE: With combined if and elif, they don't account for the year 1994, you'll get no output
#   print("You are a millenial.")            #NOTE: Added >= to if so it would include 1995
# elif year > 1995:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? ")) #NOTE: To evaluate below, input needs to be saved as an int
# if age > 18:
#     print(f"You can drive at age {age}.") #NOTE: IndentationError: expected an indented block, added an indent to the print statement
#     #NOTE: Missing an f to denote it's an f-string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) #NOTE: Using == is an evaluation, changed to = for assignment
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) #NOTE: append needed to be indented to be carried out in the for loop
#   print(b_list)

# mutate([1,2,3,5,8,13])