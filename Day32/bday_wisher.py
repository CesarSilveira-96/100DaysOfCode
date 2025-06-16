##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random

USER_EMAIL = "testepythoncesar@gmail.com"
USER_PW = "wehmogqtrsvhtpzh"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today = (month,day)

def send_email(receiver_email,message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PW)
        connection.sendmail(
            from_addr=USER_EMAIL,
            to_addrs=receiver_email,
            msg=f"Subject: Happy Anniversary! \n\n {message}"
        )

data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient="records")

for i in range(0,len(birthdays_dict)):
    bday = (birthdays_dict[i]["month"],birthdays_dict[i]["day"])
    if bday == today:
        letter_number = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_number}.txt", mode="r") as letter_file:
            letter_content = letter_file.read()
        bday_letter = letter_content.replace("[NAME]",birthdays_dict[i]["name"])
        send_email(receiver_email=birthdays_dict[i]["email"],message=bday_letter)
