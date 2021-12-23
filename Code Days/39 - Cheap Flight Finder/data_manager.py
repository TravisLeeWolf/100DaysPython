import requests

ENDPOINT = "SHEETY ENDPOINT"
AUTH_CODE = "AUTH CODE"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.endpoint = ENDPOINT
        self.header = {
            "Authorization": AUTH_CODE
        }
        self.sheetData = ""
        self.getPosts()

    def getPosts(self):
        response = requests.get(self.endpoint, headers=self.header)
        response.raise_for_status()
        self.data = response.json()
        self.sheetData = self.data["prices"]

    def updateIataCode(self, id, text):
        endpointWithId = f"{self.endpoint}/{str(id)}"
        body = {
            "price": {
                "iataCode": text
            }
        }
        response = requests.put(endpointWithId, json=body, headers=self.header)
        response.raise_for_status()