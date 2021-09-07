from time import time
from selenium import webdriver
import time

CHROME_DRIVER_PATH = "chromedriver.exe"
INSTAGRAM_USERNAME = "USERNAME"
INSTAGRAM_PASSWORD = "PASSWORD"

INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.account = ""

    def login(self) -> None:
        self.driver.get(INSTAGRAM_URL)
        time.sleep(2)
        inputUsername = self.driver.find_element_by_name("username")
        inputUsername.send_keys(INSTAGRAM_USERNAME)
        inputPassword = self.driver.find_element_by_name("password")
        inputPassword.send_keys(INSTAGRAM_PASSWORD)
        loginButton = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        loginButton.click()
        time.sleep(2)
        saveInfoButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        saveInfoButton.click()
        time.sleep(2)
        noNotificationsButton = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        noNotificationsButton.click()

    def find_followers(self) -> None:
        pass
    
    def follow(self) -> None:
        pass