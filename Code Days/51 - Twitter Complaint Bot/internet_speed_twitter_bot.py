from selenium import webdriver
import time

CHROME_DRIVER_PATH = "chromedriver.exe"

TWITTER_USERNAME = "USERNAME"
TWITTER_PASSWORD = "PASSWORD"

class InternetSpeedTwitterBot:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def getInternetSpeed(self) -> None:
        speedTestURL = "https://www.speedtest.net/"
        self.driver.get(speedTestURL)
        goButton = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        goButton.click()
        time.sleep(60)
        downSpeed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = downSpeed.text
        upSpeed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = upSpeed.text

    def tweet_at_provider(self, message) -> None:
        twitterURL = "https://twitter.com"
        self.driver.get(twitterURL)
        time.sleep(5)
        signInButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span')
        signInButton.click()
        usernameSignInButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a')
        usernameSignInButton.click()
        time.sleep(10)
        inputUsername = self.driver.find_element_by_name("session[username_or_email]")
        inputUsername.send_keys(TWITTER_USERNAME)
        inputPassword = self.driver.find_element_by_name("session[password]")
        inputPassword.send_keys(TWITTER_PASSWORD)
        loginButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        loginButton.click()
        time.sleep(10)
        composeTweetButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        composeTweetButton.click()
        time.sleep(2)
        tweetInput = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweetInput.send_keys(message)
        tweetThisButton = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweetThisButton.click()
        
        self.driver.quit()

