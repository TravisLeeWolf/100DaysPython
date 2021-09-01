from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

webpageData = response.text

soup = BeautifulSoup(webpageData, "html.parser")
articles = soup.findAll(name="a", class_="storylink")
articleLinks = []
articleTexts = []

for article in articles:
    link = article.get("href")
    articleLinks.append(link)
    text = article.getText()
    articleTexts.append(text)

articleUpvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

highestUpvotes = max(articleUpvotes)
atIndex = articleUpvotes.index(highestUpvotes) + 1

print(f"Check this article out!\n{articleTexts[atIndex]}\n{articleLinks[atIndex]}")


