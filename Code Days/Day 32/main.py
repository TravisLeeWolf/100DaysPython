from email import message
import smtplib

myEmail = "testSender@gmail.com"
password = "test"
sendToEmail = "testReciever@hotmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection: # For Hotmail: smtp.live.com
    connection.starttls()
    connection.login(user=myEmail, password=password)
    connection.sendmail(from_addr=myEmail,
                        to_addrs=sendToEmail,
                        msg="Subject:Hello\n\nThis is another test.")
