from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Devs\chromedriver.exe"
s = Service(chrome_driver_path)

class InternetSpeedTwitterBot:

    def __init__(self, s):
        self.driver = webdriver.Chrome(service=s)
        self.down = 0
        self.up = 0



    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()
        time.sleep(80)
        down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        # print(int(down.text))
        # print(int(up.text))
        self.down = down.text
        self.up = up.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        sign_with_google = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]")
        sign_with_google.click()

bot = InternetSpeedTwitterBot(s)
# print(bot.down, bot.up)
# bot.get_internet_speed()
# print(bot.down, bot.up)
bot.tweet_at_provider()