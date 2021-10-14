import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # If any connection error occur this will raise the error

data = response.json() # Getting the json data from the API

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

issPosition = (longitude, latitude)
print(issPosition)