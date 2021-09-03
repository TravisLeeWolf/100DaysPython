from selenium import webdriver

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articleCount = driver.find_element_by_css_selector("#articlecount > a:nth-child(1)")
print(articleCount.text)

driver.quit()