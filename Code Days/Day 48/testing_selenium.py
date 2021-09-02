from selenium import webdriver

chromeDriverPath = "chromedriver.exe"
braveBrowserPath = "brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = braveBrowserPath
option.add_argument("--incognito") #OPTIONAL
# option.add_argument("--headless") #OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=option)

browser.get("https://www.duckduckgo.com")

# browser.close()
browser.quit()