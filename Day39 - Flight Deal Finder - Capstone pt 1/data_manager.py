import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/33e458b9e5da9d88d15a1f6b8e0cc583/flightDeals/prices"
SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        header = {
            "Authorization": f"Basic {SHEETY_AUTH_TOKEN}"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        # response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            header = {
                "Authorization": f"Basic {SHEETY_AUTH_TOKEN}"
            }
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=header
            )
            print(response.text)

    def update_destination_price(self, city_id, new_price):
        """
        Atualiza o valor do lowestPrice na planilha para o ID da cidade especificado.
        """
        header = {
            "Authorization": f"Basic {SHEETY_AUTH_TOKEN}"
        }
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{city_id}",
            json=new_data,
            headers=header
        )
        print(f"Updated lowestPrice for ID {city_id} to {new_price}. Response: {response.text}")