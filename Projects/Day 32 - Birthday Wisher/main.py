##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from random import choice
import smtplib

templateLetters = [".\letter_templates\letter_1.txt", ".\letter_templates\letter_2.txt", ".\letter_templates\letter_1.txt"]
myEmail = "testSender@gmail.com"
password = "test"

# 1. Read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdayList = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for i in range(0, len(birthdayList)):
    if birthdayList[i]["month"] == now.month and birthdayList[i]["day"] == now.day:
        birthdaysToday = birthdayList[i]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
chosenLetterFileName = choice(templateLetters)
with open(chosenLetterFileName, "r") as data:
    letterText = data.read()
myLetter = letterText.replace("[NAME]", birthdaysToday["name"])

# 4. Send the letter generated in step 3 to that person's email address.
try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail, password=password)
        connection.sendmail(from_addr=myEmail,
                            to_addrs=birthdaysToday["email"],
                            msg=f"Subject:Happy Birthday!\n\n{myLetter}")
except:
    print("Issue with sending email.")
else:
    print(f"Email sent successfully!")



