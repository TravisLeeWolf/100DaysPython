with open("file1.txt") as dataFile1:
    firstDataList = dataFile1.readlines()
    firstListOfNumbers = [int(stringNumber.replace("\n", "")) for stringNumber in firstDataList]

with open("file2.txt") as dataFile2:
    secondDataList = dataFile2.readlines()
    secondListOfNumbers = [int(stringNumber.replace("\n", "")) for stringNumber in secondDataList]

result = [number for number in firstListOfNumbers if number in secondListOfNumbers]

# Write your code above 👆

print(result)