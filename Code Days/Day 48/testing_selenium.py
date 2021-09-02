from selenium import webdriver

chromeDriverPath = "chromedriver.exe"
braveBrowserPath = "brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = braveBrowserPath
option.add_argument("--incognito") #OPTIONAL
# option.add_argument("--headless") #OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=option)

browser.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
itemPrice = browser.find_element_by_id("priceblock-ourprice")
print(itemPrice.text)

# browser.close()
browser.quit()