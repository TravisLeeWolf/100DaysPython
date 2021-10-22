import requests
from twilio.rest import Client

# For OpenWeatherMaps
api = "OpenWeatherMaps API"
# For Twilio SMS
account_sid = "Twilio SMS ID"
auth_token = "Twilio SMS Token"

longitude = "Location LONG"
latitude = "Location LAT"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "exculde": "current,minutely,daily",
    "units": "metric",
    "appid": api
}

reponse = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
reponse.raise_for_status()

data = reponse.json()
hourly = data["hourly"]
itWillRain = False
for _ in range(0, 12):
    if hourly[_]["weather"][0]["id"] < 700:
        itWillRain = True

if itWillRain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="Your Number",
        from_="Test Number",
        body="It will rain today, remember to bring an umbrella! ☔")
    print(message.status)
