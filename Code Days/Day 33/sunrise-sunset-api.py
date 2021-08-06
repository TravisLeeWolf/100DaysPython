import requests
import datetime

MY_LAT = 34.385204
MY_LONG = 132.455292

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# Use multiple split to format only the hour in our variables
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

timeNow = datetime.datetime.now()
print(f"Current hour: {timeNow.hour}, sunrise: {sunrise}, sunset: {sunset}.")