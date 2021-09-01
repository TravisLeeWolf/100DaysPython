from turtle import heading
from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as myFile:
    contents = myFile.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.prettify())

allAnchorTags = soup.find_all(name="a")
for tag in allAnchorTags:
    # print(tag.getText())
    print(tag.get("href"))

# mainHeading = soup.find(name="h1", id="name")
# print(mainHeading)

# classIsHeading = soup.find(class_="heading") # NOTE: use class_ to avoid a conflict with Python class method
# print(classIsHeading.getText())

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)

