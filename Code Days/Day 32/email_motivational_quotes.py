from random import choice
import datetime as dt
import smtplib


myEmail = "testSender@gmail.com"
password = "test"
sendToEmail = "testReciever@hotmail.com"

#--- Get list of quotes and pick a quote ---#
with open("quotes.txt") as data:
    quoteList = data.readlines()
    chosenQuote = choice(quoteList)


#--- Check if the current day is Friday ---#
now = dt.datetime.now()
if now.weekday() == 4:
    myMessage = f"Subject:Friday Motivational Quote!\n\n{chosenQuote}"
    #--- Sending the email ---#
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myEmail, password=password)
            connection.sendmail(from_addr=myEmail,
                                to_addrs=sendToEmail,
                                msg=myMessage)
    except:
        print("There was an issue sending the email.")
    else:
        print("Message sent successfully!")

else:
    print("Wait till Friday for your motivational quote.")



