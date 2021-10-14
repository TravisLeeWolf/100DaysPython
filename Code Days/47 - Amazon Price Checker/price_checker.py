import requests
from bs4 import BeautifulSoup
import smtplib

TARGET_PRICE = 120
SENDER_EMAIL = "SENDER EMAIL"
SENDER_PASSWORD = "SENDER PASSWORD"
RECIEVER_EMAIL = "RECIEVER EMAIL"

endpoint = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(endpoint, headers=headers)
response.raise_for_status()

webSoup = BeautifulSoup(response.text, "html.parser")
itemPrice = webSoup.select_one(selector="#priceblock_ourprice").get_text()
itemPrice = float(itemPrice[1:])

productTitle = webSoup.select_one(selector="#productTitle").get_text()

if itemPrice < TARGET_PRICE:
    message = (f"{productTitle} is now ${itemPrice}!\nBuy it here: {endpoint}").encode()
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
                messageToSend = (f"Subject:Amazon Price Alert!\n\n{message}")
                connection.sendmail(from_addr=SENDER_EMAIL,
                                    to_addrs=RECIEVER_EMAIL,
                                    msg=messageToSend)
    except:
        print("There was an issue sending the email.")
    else:
        print("Email sent successfully!")