import pandas

studentScoresDict = {
    "student": ["Tom", "Mary", "Bob"],
    "score": [56, 76, 98]
}

studentDF = pandas.DataFrame(studentScoresDict)
print(studentDF)

# Loop through rows of a data frame
for (index, row) in studentDF.iterrows():
    if row.student == "Bob":
        print(row.score)