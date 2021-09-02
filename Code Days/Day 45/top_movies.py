import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/list/ls055592025/")
response.raise_for_status()
webSoup = BeautifulSoup(response.text, "html.parser")

articles = webSoup.find_all(class_="lister-item-header")
movies = []
for article in articles:
    text = article.find(name="a").get_text()
    movies.append(text)

with open("movies.txt", mode="w") as myFile:
    for movie in movies:
        myFile.write(f"{movie}\n")
