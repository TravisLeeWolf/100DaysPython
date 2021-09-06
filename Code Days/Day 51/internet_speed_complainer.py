from selenium import webdriver
from selenium.webdriver.common.keys import Keys

IDEAL_UP_SPEED = 100
IDEAL_DOWN_SPEED = 100
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"

CHROME_DRIVER_PATH = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)