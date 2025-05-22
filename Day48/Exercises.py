from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach",True)


# # provide location where chrome stores profiles
# chrome_options.add_argument("user-data-dir=C:\\Users\\cesar\\AppData\\Local\\Google\\Chrome\\User Data")
#
# # provide the profile name with which we want to open browser
# chrome_options.add_argument("profile-directory=Teste Python")

driver = webdriver.Chrome(options=chrome_options)
# BARNES AND NOBLE SITE
# driver.get("https://www.barnesandnoble.com/w/sunrise-on-the-reaping-suzanne-collins/1145703863?ean=9781546171461")
# price_whole = driver.find_element(By.CLASS_NAME, "price")
# print(f"The price is {price_whole.text}")

# PYTHON SITE
# driver.get("https://www.python.org/")
# # search_bar = driver.find_element(By.NAME, value="q")
# # print(search_bar.get_attribute("placeholder"))
# # button = driver.find_element(By.ID, "submit")
# # print(button.size)
# # documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# # print(documentation_link.text)
# # button_link = driver.find_element(By.XPATH,'//*[@id="submit"]')
# # print(button_link.text)
# # upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul li")
# # for i in range(0, len(upcoming_events)):
# #     print (upcoming_events[i].text)
# event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for date in event_dates:
#     print(date.text)
# event_names = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget li a")
# for name in event_names:
#     print(name.text)
# events_dict = {}
# # events_dict = { # --> Dict Comprehension
# #     n: {
# #         "time": event_dates[n].text,
# #         "name": event_names[n].text
# #     }
# #     for n in range(len(event_dates))
# # }
#
# for n in range(len(event_dates)):
#     events_dict[n] = {
#         "time":f"{event_dates[n].text}",
#         "name":f"{event_names[n].text}"
#     }
#
# print(events_dict)

# WIKIPEDIA SITE - INTERACTING WITH WEBPAGES
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# print(driver.current_url)  # Deve imprimir a URL correta

# articles = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/a[1]')
# print(int(number_of_articles.text.replace(" ","")))

#find elements by Link Text
# arts_category = driver.find_element(By.LINK_TEXT, "Arte")
# arts_category.click()

# IN GOOGLE.COM
# driver.get("https://google.com")

# find Search <input> by name
# Wait until the search input is visible
# search_input = driver.find_element(By.NAME, "search")
#
#
# # Type a search query
# search_input.send_keys("Python")
# # Submit search
# search_input.send_keys(Keys.ENTER)
# search_input.send_keys(Keys.ENTER)

#<<<<<<<<<<<<<<<<<<<<< APP BREWERY EXERCISE >>>>>>>>>>>>>>>>>>>>>>>>>>
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name_input = driver.find_element(By.NAME, "fName")
first_name_input.send_keys("Cesar")
last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("Teste")
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("testepythoncesar@gmail.com")
email_input.send_keys(Keys.ENTER)
sign_bt = driver.find_element(By.CLASS_NAME, "button")
# sign_bt.click()


driver.quit()