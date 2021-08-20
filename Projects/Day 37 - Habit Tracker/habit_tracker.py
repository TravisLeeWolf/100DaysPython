import requests
from datetime import datetime

USERNAME = "leewolftest2"

# NOTE: STEP ! - Creating a user
pixelaEndpoint = "https://pixe.la/v1/users"

userParams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# NOTE: This post is to create a user so it only needs to be run once
# response = requests.post(url=pixelaEndpoint, json=userParams)
# print(response.text)

# NOTE: STEP 2 - Creating a graph
graphEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"

graphConfig = {
    "id": "graph01",
    "name": "Studied Japanese",
    "unit": "days",
    "type": "int",
    "color": "ajisai"
}

# More secure than just passing the token or api key in the header
headers = {
    "X-USER-TOKEN": TOKEN
}

# NOTE: This post is to create a graph so it only needs to be run when you want to create a graph
# response = requests.post(url=graphEndpoint, json=graphConfig, headers=headers)
# print(response.text)

pixelEndpoint = f"{graphEndpoint}/{graphConfig['id']}"

today = datetime.now()

pixelConfig = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

response = requests.post(url=pixelEndpoint, json=pixelConfig, headers=headers)
print(response.text)