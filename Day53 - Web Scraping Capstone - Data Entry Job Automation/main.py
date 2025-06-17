from time import sleep
import dotenv
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
dotenv.load_dotenv()
FORMS_LINK = os.environ["FORMS_LINK"]
ZILLOW_URL = os.environ["ZILLOW_URL"]

response = requests.get(ZILLOW_URL)
soup = BeautifulSoup(response.text, "html.parser")
# all_houses_info = soup.select("ul.List-c11n-8-84-3-photo-cards")
# pp(all_houses_info)
addresses = soup.select("ul.List-c11n-8-84-3-photo-cards address")
address_list = []
prices = soup.select("ul.List-c11n-8-84-3-photo-cards span.PropertyCardWrapper__StyledPriceLine")
price_list = []
house_links = soup.select("ul.List-c11n-8-84-3-photo-cards a.StyledPropertyCardDataArea-anchor")
links_list = []
for i in range(len(addresses)):
    clean_address = addresses[i].get_text(strip=True).replace(" |",",")
    clean_price = (prices[i].get_text(strip=True).replace("+/mo","").replace("/mo","").
                   replace("+ 1bd","").replace("+ 1 bd",""))
    address_list.append(clean_address)
    price_list.append(clean_price)
    links_list.append(house_links[i].get("href"))

print(address_list)
print(price_list)
print(links_list)

# >>>>>>>>>>>> Setting Up Selenium Webdriver <<<<<<<<<<<<<<<<<

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(FORMS_LINK)
for i in range(len(address_list)):
    sleep(3)
    address_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/'
                                                 'div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[i])
    price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/'
                                               'div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[i])
    link_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                               'div/div[1]/div/div[1]/input')
    link_input.send_keys(links_list[i])
    sleep(1)
    send_bt = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Enviar')]")
    send_bt.click()
    # Start nem forms
    sleep(3)
    new_submission = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    new_submission.click()

