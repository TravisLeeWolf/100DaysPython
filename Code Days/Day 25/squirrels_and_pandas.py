import pandas

data = pandas.read_csv("squirrel_data.csv")


cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]

cinnamonCount = cinnamon["Unique Squirrel ID"].count()
grayCount = gray["Unique Squirrel ID"].count()
blackCount = black["Unique Squirrel ID"].count()

squirrelCount = {
    "Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamonCount, grayCount, blackCount]
}

countData = pandas.DataFrame(squirrelCount)
print(countData)
countData.to_csv("squirrel_count.csv")