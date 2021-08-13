import requests
from newsapi import NewsApiClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"



STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alphaParams = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": ALPHA_API
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params=alphaParams)
response.raise_for_status()
data = response.json()

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterdayClose = float(data["Time Series (Daily)"]["2021-08-12"]["4. close"])
print(f"Yesterday's price: ${yesterdayClose: .2f}")

#TODO 2. - Get the day before yesterday's closing stock price
beforeYesterdayClose = float(data["Time Series (Daily)"]["2021-08-11"]["4. close"])
print(f"Day before yesterday's price: ${beforeYesterdayClose: .2f}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterdayClose - beforeYesterdayClose
print(f"Difference in above price: ${difference: .2f}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentageDifference = (difference / yesterdayClose) * 100
print(f"Percentage difference: {percentageDifference: .2f}%")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if (percentageDifference) > 5:

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    newsApi = NewsApiClient(api_key=NEWS_API)
    articles = newsApi.get_everything(q="tesla", from_param="2021-07-13")
    for _ in range(3):
        print(articles['articles'][_]['title'])

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

