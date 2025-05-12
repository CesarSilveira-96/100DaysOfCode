import smtplib
import datetime as dt
import random

# BIRTHDAY_WISHER_PASSWORD = ""
#
YAHOO_USER = "testepythoncesar@yahoo.com"

GMAIL_USER = "testepythoncesar@gmail.com"
GMAIL_PW = "iyzdadrqmcmstapw"

## Using datetime (as dt)
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
#
# date_of_birth = dt.datetime(year= 1996, month= 12, day= 18, hour=10)
# print(date_of_birth)

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PW)
        connection.sendmail(
            from_addr=GMAIL_USER,
            to_addrs=YAHOO_USER,
            msg=f"Subject: Monday Motivation Phrase! \n\n {quote}"
        )

with open("quotes.txt", mode="r") as quotes_file:
    quotes_data = quotes_file.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()
# counter = 0


if day_of_week == 0:
    quote = random.choice(quotes_data)
    send_email(quote)
    # quotes_data.remove(quotes_data[counter])
    # if counter < 102:
    #     counter += 1

