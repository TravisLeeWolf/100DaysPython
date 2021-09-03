from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articleCount = driver.find_element_by_css_selector("#articlecount a")
# articleCount.click()

# allPortals = driver.find_element_by_link_text("All portals")
# allPortals.click()

# searchBar = driver.find_element_by_name("search")
# searchBar.send_keys("Python")
# searchBar.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element_by_name("fName")
firstName.send_keys("Bob")
lastName = driver.find_element_by_name("lName")
lastName.send_keys("Builder")
email = driver.find_element_by_name("email")
email.send_keys("bob@builder.com")

submitButton = driver.find_element_by_css_selector("body > form > button")
submitButton.click()

driver.quit()

