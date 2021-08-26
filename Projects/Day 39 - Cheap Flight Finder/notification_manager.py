import smtplib
from flight_data import FlightData

MY_EMAIL = "SENDER EMAIL"
PASSWORD = "PASSWORD"
SEND_TO_EMAIL = "RECIEVER EMAIL"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.flightList = []
        self.emailsToSend = []

    def getFlightList(self):
        flightData = FlightData()
        if len(flightData.notificationFlightList) > 0:
            self.flightList = flightData.notificationFlightList

    def composeEmail(self):
        self.getFlightList()
        for flight in self.flightList:
            message = f"Only £{flight[0]} to fly from {flight[1]}-{flight[2]} to {flight[3]}-{flight[4]}, from {flight[5]} to {flight[6]}."
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

