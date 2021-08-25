import requests



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = "https://tequila-api.kiwi.com"
        self.header = {
            "apikey": API_KEY
        }
        self.cityCode = ""

    def searchCity(self, cityName):
        query = {"term": cityName, "location_types": "city"}
        response = requests.get(f"{self.endpoint}/locations/query", headers=self.header, params=query)
        data = response.json()
        self.cityCode = data["locations"][0]["code"]