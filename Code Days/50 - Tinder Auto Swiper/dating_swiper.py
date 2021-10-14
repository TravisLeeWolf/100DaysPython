from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import time

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

chromeDriverPath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("https://tinder.com/")

signInButton = driver.find_element_by_css_selector("#q-2020625691 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div:nth-child(2) > div.H\(40px\).Px\(28px\) > a")
signInButton.click()

time.sleep(1)

withFacebook = driver.find_element_by_css_selector("#q545960529 > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div:nth-child(2) > button")
withFacebook.click()

time.sleep(2)

facebookWindow = driver.window_handles[1]
driver.switch_to.window(facebookWindow)

emailInput = driver.find_element_by_name("email")
passwordInput = driver.find_element_by_name("pass")
logInButton = driver.find_element_by_name("login")

emailInput.send_keys(EMAIL)
passwordInput.send_keys(PASSWORD)
logInButton.click()

mainWindow = driver.window_handles[0]
driver.switch_to.window(mainWindow)

time.sleep(5)

allowLocationButton = driver.find_element_by_css_selector("#q545960529 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$primary-gradient\).button--primary-shadow.StyledButton.Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)")
allowLocationButton.click()

time.sleep(1)

dontAllowNotificationsButton = driver.find_element_by_css_selector("#q545960529 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Fw\(\$semibold\).focus-button-style.W\(a\).C\(\$c-bluegray\)")
dontAllowNotificationsButton.click()

time.sleep(1)

cookiesButton = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[2]/div/div/div[1]/button')
cookiesButton.click()

time.sleep(10)
likeButton = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button')
for _ in range(5):
    try:
        time.sleep(2)
        likeButton.click()
    except exceptions.ElementClickInterceptedException:
        notInterestedButton = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div[2]/button[2]')
        notInterestedButton.click()
    except exceptions.NoSuchElementException:
        time.sleep(5)
        continue

driver.quit()