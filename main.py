from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




CHROME_DRIVER_PATH="C:\ChromeWebDriver\chromedriver.exe"



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

service = Service("C:\ChromeWebDriver\chromedriver.exe")

class InternetSpeedTwitterBot:
    def __init__(self,driver):
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.up=0
        self.down=0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.events=self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        self.events.click()
        time.sleep(45)
        self.down=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down,self.up)



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
        events.send_keys(f"My current download speed is: {self.down} and upload speed is: {self.up} ")
        time.sleep(2)
        events=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        events.click()
        time.sleep(2)




bot=InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
