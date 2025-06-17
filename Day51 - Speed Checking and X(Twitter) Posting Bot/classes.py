from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import dotenv
import os

dotenv.load_dotenv()

X_EMAIL = os.environ["X_EMAIL"]
X_PASSWORD = os.environ["X_PASSWORD"]
X_USERNAME = os.environ["X_USERNAME"]
class Classes:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/pt")
        sleep(2)
        start_bt = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_bt.click()
        sleep(60)
        download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/'
                                                      'div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                      'div[2]/span')
        download_speed = float(download.text)
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/'
                                                    'div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/'
                                                    'div/div[2]/span')
        upload_speed = float(upload.text)
        print(download_speed)
        print(upload_speed)
        self.down = download_speed
        self.up = upload_speed

    def post_at_x(self):
        self.driver.get("https://twitter.com/")
        sleep(2)
        enter_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                        'div[1]/div/div/div[3]/div[4]/a/div')
        enter_button.click()
        sleep(3)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                         'div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/'
                                                         'div[2]/div/input')
        email_input.send_keys(f"{X_USERNAME}")
        email_input.send_keys(Keys.ENTER)
        sleep(2)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                            'div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/'
                                                            'label/div/div[2]/div[1]/input')
        password_input.send_keys(f"{X_PASSWORD}")
        password_input.send_keys(Keys.ENTER)
        sleep(5)
        post_input = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                       'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/'
                                                       'div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/'
                                                       'div[2]/div/div/div/div')
        post_input.send_keys(f"Hey Super 15 Telefônica, my internet Download speed is only{self.down}mbps"
                             f" and the Upload Speed {self.up}mbps.\n"
                             f"Fix That ASAP.")
        post_bt = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                    'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/'
                                                    'div/div/button/div/span/span')
        post_bt.click()
        sleep(15)
        self.driver.quit()