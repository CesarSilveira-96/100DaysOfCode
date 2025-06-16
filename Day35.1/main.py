import requests
from twilio.rest import Client

# Twilio info
account_sid = "ACe30ca55b1bcd7cbb68d0a112aec5ffb1"
auth_token = "8f3bfcd4bfd6eb96a91b4c3e5252e3fa"

#OWM info
API_KEY = "444534fd32833ffbe20106db70d33020"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
MY_LAT = 39.933365
MY_LONG = 32.859741
weather_params = {
    "lat":MY_LAT,
    "lon": MY_LONG,
    "appid":API_KEY,
    "cnt": 4,
    "units":"metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

def will_it_rain():
    rainy = False
    for i in range(0,3):
        weather_condition = int(weather_data["list"][i]["weather"][0]["id"])
        if weather_condition < 700:
            rainy = True
    if rainy:
        client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     from_="+14155238886",
        #     body="Bring an umbrella.",
        #     to="+5535984733337"
        # )
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body= "It will rain outside! Bring an umbrella.",
            to="whatsapp:+553584733337"
        )

        print(message.status)
will_it_rain()

#