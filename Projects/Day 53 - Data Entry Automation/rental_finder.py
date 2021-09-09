import requests
from bs4 import BeautifulSoup

CHROME_DRIVER_PATH = "chromedriver.exe"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

class RentalFinder:

    def __init__(self) -> None:
        self.url = ""
        self.webSoup = ""
        self.links = []
        self.prices = []
        self.addresses = []

    def getWebSoup(self):
        response = requests.get(self.url, headers=HEADERS)
        self.webSoup = BeautifulSoup(response.text, "html.parser")

    

