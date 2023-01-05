from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests






CHROME_DRIVER_PATH="C:\ChromeWebDriver\chromedriver.exe"



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

service = Service("C:\ChromeWebDriver\chromedriver.exe")

class InternetSpeedTwitterBot:
    def __init__(self,driver):
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.lat=0
        self.lng=0
        self.min=0
        self.max=0
    def coordinates(self):
        KEY = 'your_key'
        city = "your_city"
        state = "your_state"
        url = f'http://www.mapquestapi.com/geocoding/v1/address?key={KEY}&location={city},{state}'

        response = requests.get(url)
        data = response.json()
        print(data['results'][0]['locations'][0]['displayLatLng'])
        self.lat=float(data['results'][0]['locations'][0]['displayLatLng']['lat'])
        self.lng=float(data['results'][0]['locations'][0]['displayLatLng']['lng'])

    def weather(self):
        appid = "your_id"
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lng}&appid={appid}')
        data = response.json()
        self.min = round((data['main']['temp_min'] - 273.15) * (9 / 5) + 32)
        self.max = round((data['main']['temp_max'] - 273.15) * (9 / 5) + 32)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        events=self.driver.find_element(By.CLASS_NAME,'r-30o5oe')
        events.click()
        time.sleep(2)
        events.send_keys("your_login")
        time.sleep(1)
        events=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        events.click()
        time.sleep(2)
        events=self.driver.find_element(By.CLASS_NAME,'r-30o5oe')
        time.sleep(2)
        events.send_keys("your_password")
        time.sleep(2)
        events.send_keys(Keys.ENTER)
        time.sleep(3)
        events=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        events.click()
        time.sleep(1)
        events=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        events.send_keys(f"The lowest temperature for today is: {self.min} F\n"
                         f"The highest temperature for today is: {self.max} F\n"
                         f"--tweeted by @twitter_bot--")
        time.sleep(2)
        events=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        events.click()
        time.sleep(2)




bot=InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.coordinates()
bot.weather()
bot.tweet_at_provider()
