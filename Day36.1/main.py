import requests
from twilio.rest import Client

SYMBOL = "NFLX"
COMPANY_NAME = "Netflix, Inc."
STOCK_API_KEY = "DQQAFONDQZMCLCBY"
NEWS_API_KEY = "60bbeb73f39a45b2bac05ab5ce926295"

twilio_account_sid = "ACe30ca55b1bcd7cbb68d0a112aec5ffb1"
twilio_auth_token = "8f3bfcd4bfd6eb96a91b4c3e5252e3fa"

# >>>>>>>>>>>>>>>>>>>> Getting Stock API Data <<<<<<<<<<<<<<<<<<<<
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":SYMBOL,
    "outputsize":"compact",
    "apikey":STOCK_API_KEY
}
stock_url = "https://www.alphavantage.co/query"

response = requests.get(stock_url, params=stock_parameters)
data = response.json()
day_before_close = float(data["Time Series (Daily)"]["2025-05-12"]["4. close"])
yesterday_open = float(data["Time Series (Daily)"]["2025-05-13"]["1. open"])
diff = yesterday_open - day_before_close
percent_diff = diff/day_before_close*100

print (diff)
print (percent_diff)

# >>>>>>>>>>>>>>>>>>>> Getting News API Data <<<<<<<<<<<<<<<<<<<<
news_parameters = {
    "qInTitle":COMPANY_NAME,
    "from":"2025-04-14",
    "sortBy":"publishedAt",
    "language":"en",
    "apiKey":NEWS_API_KEY
}
news_url = "https://newsapi.org/v2/everything"

# if percent_diff > 5 or -5 > percent_diff:
news_response = requests.get(news_url, params=news_parameters)
news_data = news_response.json()
articles_title_list = [news_data["articles"][i]["title"] for i in range(0,3)]
articles_content_list = [news_data["articles"][i]["content"] for i in range(0,3)]
articles_url_list = [news_data["articles"][i]["url"] for i in range(0,3)]

# >>>>>>>>>>>>>>>>>>>> Sending msg via Twilio <<<<<<<<<<<<<<<<<<<<
up_down = None
if percent_diff > 0:
    up_down = "🔺"
elif percent_diff < 0:
    up_down = "🔻"
if -5 > percent_diff or percent_diff > 5:
    for nmb in range (0, len(articles_title_list)):
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            from_="+14235564822",
            body=f"{SYMBOL}: {up_down}5%"
                 f"Title: {articles_title_list[nmb]}\n"
                 f"Briefing: {articles_content_list[nmb]}\n"
                 f"url: {articles_url_list[nmb]}",
            to="+5535984733337"
        )
        print(message.status)

