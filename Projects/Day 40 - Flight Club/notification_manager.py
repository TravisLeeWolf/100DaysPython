from signup_manager import SignupManager
import smtplib

MY_EMAIL = "SENDER EMAIL"
PASSWORD = "PASSWORD"

class NotificationManager:

    def __init__(self):
        self.message = ""
        users = SignupManager()
        self.userList = users.getUserDetailsToList()

    def send_email(self, message, link):
        messageAndLink = f"{message}\n{link}"
        try:
           with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                for email in self.userList:
                    messageToSend = (f"Subject:Low price alert!\n\n{messageAndLink}").encode("utf-8")
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=email["email"],
                                        msg=messageToSend)
        except:
            print("Issue with sending email.")
        else:
            print("Email sent successfully!")
        
        
