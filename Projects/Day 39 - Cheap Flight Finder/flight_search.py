from tkinter.constants import S
import requests
from datetime import datetime, timedelta

API_KEY ="API KEY"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = "https://tequila-api.kiwi.com"
        self.header = {
            "apikey": API_KEY
        }
        self.cityCode = ""
        self.flightData = ""

    def searchCity(self, cityName):
        cityEndpoint = f"{self.endpoint}/locations/query"
        query = {
            "term": cityName,
            "location_types": "city"
        }
        response = requests.get(cityEndpoint, headers=self.header, params=query)
        data = response.json()
        self.cityCode = data["locations"][0]["code"]

    def searchFlights(self, destinationCode, maxPrice):
        flightsEndpoint = f"{self.endpoint}/v2/search"
        tomorrow = datetime.now() + timedelta(hours=24)
        sixMonthsAhead = datetime.now() + timedelta(days=180)
        query = {
            "fly_from": "LON",
            "fly_to": destinationCode,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": sixMonthsAhead.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "price_to": maxPrice,
            "max_stopovers": 0,
            "limit": 1
        }
        response = requests.get(flightsEndpoint, headers=self.header, params=query)
        self.flightData = response.json()
        if self.flightData["_results"] > 0:
            self.flightData = self.flightData["data"][0]
        else:
            self.flightData = ""
    