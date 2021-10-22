import smtplib
from datetime import datetime

MY_EMAIL = "SENDER EMAIL"
PASSWORD = "SENDER PASSWORD"
SEND_TO_EMAIL = "RECIEVER EMAIL"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.flightList = []
        self.emailsToSend = []

    def getFlightList(self, flightData):
        if len(flightData) > 0:
            self.flightList = flightData

    def composeEmail(self):
        for flight in self.flightList:
            # NOTE: Use string strip instead
            dateTo = flight[5][:10]
            dateFrom = flight[6][:10]
            message = f"Only \u00A3{flight[0]} to fly from {flight[1]}-{flight[2]} to {flight[3]}-{flight[4]}, from {dateTo} to {dateFrom}."
            self.emailsToSend.append(message)

    def sendMail(self):
        self.composeEmail()
         
        try:
           with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                for email in self.emailsToSend:
                    message = (f"Subject:Low price alert!\n\n{email}").encode("utf-8")
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=SEND_TO_EMAIL,
                                        msg=message)
        except:
            print("Issue with sending email.")
        else:
            print("Email sent successfully!")

