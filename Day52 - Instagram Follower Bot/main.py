from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import dotenv
import os

dotenv.load_dotenv()

SIMILAR_ACCOUNT = "cazetv"
IG_EMAIL = os.environ["IG_EMAIL"]
IG_PASSWORD = os.environ["IG_PASSWORD"]
IG_USERNAME = os.environ["IG_USERNAME"]

class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")

        sleep(2)
        user_input = self.driver.find_element(By.XPATH, '//input[@name="username"]')
        user_input.send_keys(f"{IG_USERNAME}")

        sleep(2)
        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_input.send_keys(f"{IG_PASSWORD}")

        enter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')))
        enter_button.click()

        sleep(8)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Agora')]")
        if save_login_prompt:
            save_login_prompt.click()


    def find_followers(self):
        sleep(2)
        # Show followers of the selected account.
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")

        sleep(4)
        followers = self.driver.find_element(By.XPATH,'//span[contains(text(), " seguidores")]')
        followers.click()

        sleep(10)
        modal_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"

        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)


    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.

        sleep(10)
        all_buttons = self.driver.find_elements(
            By.XPATH, '//button[normalize-space()="Seguir"]'
        )

        for button in all_buttons:
            try:
                button.click()
                sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except EC:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()


#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

