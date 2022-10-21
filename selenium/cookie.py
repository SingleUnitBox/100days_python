from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Devs\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


# cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
# buy_list.append(cursor.text.split()[-1])
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
item_ids= item_ids[0:len(item_ids)-1]
item_ids.reverse()
print(item_ids)



five_sec = time.time() + 2
five_mins = time.time() + 60*5

switch = True
while switch:
    cookie.click()

    if time.time() > five_sec:

        buy_list = []
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        #print(store)

        for item in store:
            element = item.text
            print(type(element))
            if element[-1].isdigit():
                cost = int(element.split("-")[1].strip().replace(",", ""))
                buy_list.append(cost)
        print(buy_list)
        buy_list.reverse()
        print(buy_list)


        money = (driver.find_element(By.ID, "money")).text
        if "," in money:
            money = money.replace(",", "")
        money = int(money)

        for item in buy_list:
            if money > item:
                print(item)
                print({item_ids[buy_list.index(item)]})
                buy = driver.find_element(By.ID, f"{item_ids[buy_list.index(item)]}")
                buy.click()
        five_sec = time.time() + 5



