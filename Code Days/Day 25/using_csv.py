# with open("weather_data.csv") as weatherDataFile:
#     weatherData = weatherDataFile.readlines()
#     print(weatherData)

## Without using pandas
# import csv
# with open("weather_data.csv") as dataFile:
#     data = csv.reader(dataFile)
#     temparatures = []
#     for row in data:
#         for row in data:
#             if row[1] != "temp":
#                 temparatures.append(int(row[1]))
#     print(temparatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# temparatures = data["temp"].to_list()
# average = sum(temparatures) / (len(temparatures))
# print(f'The average temperature was: {average: .1f}\u00B0C')

## Using pandas for average
# print(data["temp"].mean())

## Getting the max value from the column
# print(data["temp"].max())
## Both are valid
# print(data.temp.max())

## Get data in a row
# print(data[data.day == "Monday"])

## Get the row that has the max temperature
# print("Day with the hottest temperature")
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# mondayTemperature = int(monday.temp)
# mondayTemperatureInF = mondayTemperature * 9/5 + 32
# print(mondayTemperatureInF)

dataDictionary = {
    "students": ["Bob", "Mary", "Tom"],
    "scores": [78, 98, 65]
}
data = pandas.DataFrame(dataDictionary)
print(data)
# data.to_csv("student_scores.csv")