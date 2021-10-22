from selenium import webdriver

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("https://www.python.org/")
events = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
eventTimes = events.find_elements_by_css_selector("time")
eventLinks = events.find_elements_by_css_selector("a")

dates = [date.get_attribute("datetime")[:10] for date in eventTimes]
links = [name.text for name in eventLinks]
driver.quit()

pythonEvents = {}

for i in range(len(links)):
    entry = {"time": dates[i], "name": links[i]}
    number = str(i)
    pythonEvents.update({number: entry})

print(pythonEvents)

