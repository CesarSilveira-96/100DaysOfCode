import requests
from datetime import datetime as dt

MY_LAT = -22.886779
MY_LNG = -46.968974

# response = requests.get(url= "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longitude)
# print(latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0
}

response = requests.get(url= f"https://api.sunrise-sunset.org/json?lat={parameters["lat"]}&lng={parameters["lng"]}&formatted={parameters["formatted"]}")
response.raise_for_status()
sun_data = response.json()
sunrise = sun_data["results"]["sunrise"].split("T")[1].split(":")
sunset = sun_data["results"]["sunset"].split("T")[1].split(":")


print(sunrise[0])
print(sunset[0])

hour_now = dt.now().hour
print(hour_now)