from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import os
import dotenv
from classes import Classes

dotenv.load_dotenv()

X_EMAIL = os.environ["X_EMAIL"]
X_PASSWORD = os.environ["X_PASSWORD"]
UP_SPEED = float(os.environ["PROMISED_UP"])
DOWN_SPEED = float(os.environ["PROMISED_DOWN"])

classes = Classes()
classes.get_internet_speed()

if classes.up < UP_SPEED or classes.down < DOWN_SPEED:
    classes.post_at_x()