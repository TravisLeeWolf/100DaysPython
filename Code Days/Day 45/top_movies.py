import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
webSoup = BeautifulSoup(response.text, "html.parser")

article = webSoup.find_all(class_="listicle-item-content")
print(article[1].prettify())