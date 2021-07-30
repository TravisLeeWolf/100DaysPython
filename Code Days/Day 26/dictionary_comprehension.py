import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

studentScores = {student:random.randint(1, 100) for student in names}
print(studentScores)

passedStudents = {student:score for (student, score) in studentScores.items() if score > 50}
print("The students below passed the test.")
print(passedStudents)