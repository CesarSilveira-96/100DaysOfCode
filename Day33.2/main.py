import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -22.886779
MY_LONG = -46.968974

# ---------------------- EMAIL SENDER ----------------------------------------------------------------------
USER_EMAIL = "testepythoncesar@gmail.com"
USER_PW = "iyzdadrqmcmstapw"

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PW)
        connection.sendmail(
            from_addr=USER_EMAIL,
            to_addrs="testepythoncesar@gmail.com",
            msg="Subject: THE ISS IS IN THE SKY!!! \n\nLook Up! The ISS should be right there!"
        )

# ---------------------- ISS POSITION ----------------------------------------------------------------------

    # >>>>>> SEARCH IN ISS API FOR POSITION <<<<<<
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# >>>>>> SEARCH IN SUNRISE/SUNSET API FOR NIGHTTIME <<<<<<
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# >>>>>> CHECK IF IT IS CURRENTLY IN POSITION AND NIGHTTIME <<<<<<
while True:
    time.sleep(60)
    if -5 <= (iss_latitude - MY_LAT) <= 5 and -5 <= (iss_longitude - MY_LONG) <= 5:
        if sunrise > time_now or sunset < time_now:
            send_email()
