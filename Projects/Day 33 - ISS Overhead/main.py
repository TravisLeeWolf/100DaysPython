import requests
from datetime import datetime, timezone
import smtplib

MY_LAT = 34.385204
MY_LONG = 132.455292

inViewingDistance = False
isDarkOut = False

myEmail = "testSender@gmail.com"
password = "test"
sendToEmail = "testReciever@hotmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

issLatitude = float(data["iss_position"]["latitude"])
issLongitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
# print(f"My position:\nLatitude: {MY_LAT} Longitude: {MY_LONG}\nISS position:\nLatitude: {issLatitude} Longitude: {issLongitude}.")
latFromMeToISS = abs(MY_LAT) - abs(issLatitude)
longFromMetoISS = abs(MY_LONG) - abs(issLongitude)
if (-5 < latFromMeToISS < 5) and (-5 < longFromMetoISS < 5):
    inViewingDistance = True
else:
    print("You're not close enough to the ISS to see it, sorry.")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

timeNow = datetime.now(tz=timezone.utc)
# print(f"It's currently {timeNow.hour}Hrs UTC, sunset is at {sunset}Hrs and sunrise at {sunrise}Hrs.")
if sunset < timeNow.hour < sunrise:
    isDarkOut = True
else:
    print("You can't see the ISS in the day time.")

if inViewingDistance and isDarkOut:
    with smtplib.SMTP("smtp.gmail.com") as connection: # For Hotmail: smtp.live.com
        connection.starttls()
        connection.login(user=myEmail, password=password)
        connection.sendmail(from_addr=myEmail,
                            to_addrs=sendToEmail,
                            msg="Subject:Tonight you can see the ISS!\n\nIt should be dark there and the ISS is currently passing over you!.")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



