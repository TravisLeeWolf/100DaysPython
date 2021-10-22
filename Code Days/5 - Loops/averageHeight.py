# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

numberOfItems = n + 1
totalHeight = 0
for height in student_heights:
    totalHeight += height

averageHeight = totalHeight/numberOfItems
print(int(averageHeight))