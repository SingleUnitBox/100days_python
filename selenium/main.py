from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Devs\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")
#driver.get("https://www.amazon.co.uk/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5N1WBH/ref=sr_1_1_sspa?crid=2EWBIVOLJY2MX&keywords=macbook&qid=1666214131&qu=eyJxc2MiOiI1LjEzIiwicXNhIjoiNS4wNiIsInFzcCI6IjMuOTUifQ%3D%3D&sprefix=macbook%2Caps%2C73&sr=8-1-spons&psc=1")
# price = driver.find_element(By.CLASS_NAME, "a-price")
# print(price.text)
#<span class="a-price-whole">899<span class="a-price-decimal">.</span></span>

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events_dict = {}

# for event in events_dates:
#     print(event.text)
#
#
# for e in events:
#     print(e.text)

for n in range(0, len(events_dates)):
    events_dict[n] = {
        "time": events_dates[n].text,
        "name": events[n].text,
    }

print(events_dict)



# //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a
# //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/a
#driver.close()
driver.quit()