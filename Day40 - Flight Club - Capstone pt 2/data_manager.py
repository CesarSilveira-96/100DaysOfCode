import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import smtplib
from pprint import pprint
# Load environment variables from .env file
load_dotenv()


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.sheety_users_token = os.environ["SHEETY_USERS_TOKEN"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        header = {
            "Authorization": f"Basic {self.sheety_users_token}"
        }
        response = requests.get(url=self.prices_endpoint, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data["prices"])
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            header = {
                "Authorization": f"Basic {self.sheety_users_token}"
            }
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers=header
            )
            print(response.text)


    def get_customer_emails(self):
        # Use the Sheety API to GET all the email data in the users tab.
        header = {
            "Authorization": f"Basic {self.sheety_users_token}"
        }
        response = requests.get(url=self.users_endpoint, headers=header)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

