from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "email"
PASSWORD = "password"

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

endpoint = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102095887&keywords=python%20developer&location=California%2C%20United%20States"

driver.get(endpoint)

homeSignInButton = driver.find_element_by_css_selector("body > div.base-serp-page > header > nav > div > a.nav__button-secondary")
homeSignInButton.click()

time.sleep(2)

emailInput = driver.find_element_by_name("session_key")
passwordInput = driver.find_element_by_name("session_password")
emailInput.send_keys(EMAIL)
passwordInput.send_keys(PASSWORD)

enterSignInButton = driver.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
enterSignInButton.click()

time.sleep(3)

jobListings = driver.find_elements_by_css_selector("a.job-card-list__title")
for job in jobListings:
    title = (job.text).lower()
    if "python" in title and "developer" in title:
        job.click()
        time.sleep(3)
        applyNowButton = driver.find_element_by_css_selector("button.jobs-save-button")
        applyNowButton.click()

driver.quit()