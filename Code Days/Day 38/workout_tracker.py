import requests
from datetime import datetime

APP_ID = "Add app id"
API_KEY = "Add api key"
SHEETY_AUTH = "Add sheety authorization"


GENDER = "gender"
WEIGHT_KG = "weight in kg"
HEIGHT_CM = "height in cm"
AGE = "age"

workout = input("What workout did you do today?\n")
now = datetime.now()
dateNow = now.strftime("%d/%m/%Y")
timeNow = now.strftime("%H:%M:%S")

exerciseEndpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheetyEndpoint = "Sheety Endpoint"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

workout_query = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exerciseEndpoint, headers=headers, json=workout_query)
response.raise_for_status()
data = response.json()

exerciseName = (data["exercises"][0]["name"]).title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

workoutToSheety = {
    "workout": {
        "date": dateNow,
        "time": timeNow,
        "exercise": exerciseName,
        "duration": duration,
        "calories": calories
    }
}

sheetyHeader = {
    "Authorization": SHEETY_AUTH
}

sheetyResponse = requests.post(sheetyEndpoint, json=workoutToSheety, headers=sheetyHeader)
print(sheetyResponse.text)
