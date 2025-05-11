import smtplib

from pyexpat.errors import messages

BIRTHDAY_WISHER_PASSWORD = ""

YAHOO_USER = "testepythoncesar@yahoo.com"
YAHOO_PW = ""

GMAIL_USER = "testepythoncesar@gmail.com"
GMAIL_PW = "iyzdadrqmcmstapw"

with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
    connection.starttls()
    connection.login(user= GMAIL_USER, password=GMAIL_PW)
    connection.sendmail(
        from_addr=GMAIL_USER,
        to_addrs=YAHOO_USER,
        msg="Subject: Python Test \n\nHello, Cesar!"
    )
