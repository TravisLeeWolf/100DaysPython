from selenium import webdriver

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
# itemPrice = driver.find_element_by_id("priceblock_ourprice")
# print(itemPrice.text)

driver.get("https://www.python.org/")
# searchBar = driver.find_element_by_name("q")
# print(searchBar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentationLink = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentationLink.text)

bugLink = driver.find_element_by_xpath('//*[@id="container"]/li[8]/ul/li[2]/a')
print(bugLink.text)

# driver.close()
driver.quit()