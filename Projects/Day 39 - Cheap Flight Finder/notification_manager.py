import smtplib
from datetime import datetime

MY_EMAIL = "sender"
PASSWORD = "pass"
SEND_TO_EMAIL = "reciever"


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
            boundForTime = datetime(flight[5]).strftime("%d - %m - %Y")
            returnTime = datetime(flight[6]).strftime("%d - %m - %Y")
            message = f"Only £{flight[0]} to fly from {flight[1]}-{flight[2]} to {flight[3]}-{flight[4]}, from {boundForTime} to {returnTime}."
            self.emailsToSend.append(message)
            print(message)

    def sendMail(self):
        self.composeEmail()
        try:
           with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                for email in self.emailsToSend:
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=SEND_TO_EMAIL,
                                        msg=f"Subject:Low price alert!\n\n{email}") 
        except:
            print("Issue with sending email.")
        else:
            print("Email sent successfully!")

