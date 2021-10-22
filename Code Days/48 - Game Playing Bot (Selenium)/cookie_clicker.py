from selenium import webdriver
import time

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("http://orteil.dashnet.org/experiments/cookie")

cookie = driver.find_element_by_id("cookie")
def getMoney():
    money = int(driver.find_element_by_id("money").text)
    return money

def getCPS():
    cps = int(driver.find_element_by_id("cps").text.split()[2])
    return cps

def getItems():
    storeItems = driver.find_elements_by_css_selector("#store b")
    return storeItems

def checkIfCanBuyItem(money, storeItems):
    pricesSTR = [item.text.split()[-1] for item in storeItems if item.text != ""]
    prices = []
    for price in pricesSTR:
        if len(price) > 3:
            price = price.replace(",", "")
        prices.append(int(price))

    for i in range(len(prices)):
        if money > prices[i]:
            me = i
    storeItems[me].click()

playGame = True
while playGame:
    for _ in range(100):
        cookie.click()
    money = getMoney()
    items = getItems()
    checkIfCanBuyItem(money, items)

driver.quit()