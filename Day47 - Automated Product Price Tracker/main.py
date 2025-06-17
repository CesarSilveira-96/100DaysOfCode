from bs4 import BeautifulSoup
import requests
import smtplib
import dotenv
import os

dotenv.load_dotenv()
SMTP_USER_EMAIL = os.environ.get("SMTP_USER_EMAIL")
SMTP_USER_PW = os.environ.get("SMTP_USER_PW")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
SMTP_ADDRESS = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")

# print("SMTP_ADDRESS:", SMTP_ADDRESS)
# print("SMTP_USER_EMAIL:", SMTP_USER_EMAIL)
# print("SMTP_USER_PW:", SMTP_USER_PW)

# URL_OFF = "https://appbrewery.github.io/instant_pot/"
URL_LIVE = "https://www.amazon.com.br/Instant-Pot-press%C3%A3o-multiuso-fritadeira/dp/B08WCLJ7JG/ref=sr_1_1"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

soup_response = requests.get(f"{URL_LIVE}", headers=header)
soup = BeautifulSoup(soup_response.text,"html.parser")
title = soup.select_one(selector="h1 span#productTitle").get_text(strip=True)
price_symbol = soup.select_one(selector="span span.a-price-symbol").get_text()
price_whole = soup.select_one(selector="span span.a-price-whole").get_text().replace(".","").replace(",",".")
price_fraction = soup.select_one(selector="span span.a-price-fraction").get_text()
price = f"{price_symbol}{price_whole}{price_fraction}"

# print(title)
# print(price_symbol)
# print(price_whole)
# print(price_fraction)

float_price = float(f"{price_whole}{price_fraction}")
print(float_price)
BUY_PRICE = 2000.00
#
if float_price < BUY_PRICE:
    message = f"{title} à venda por {price}!"
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        result = connection.login(SMTP_USER_EMAIL, SMTP_USER_PW)
        connection.sendmail(
            from_addr=SMTP_USER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL_LIVE}".encode("utf-8")
        )