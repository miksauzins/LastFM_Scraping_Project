from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

service=Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


hasLoggedIn = False

driver.get("https://www.last.fm/")
driver.implicitly_wait(2)

if(driver.current_url.endswith("/home")):
    hasLoggedIn = true
else:
    driver.get("https://www.last.fm/login")
    driver.implicitly_wait(5)
    time.sleep(5)
    try: 
        cookieBarIsPresent = driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookieBarIsPresent.click()
        print("found")
    except NoSuchElementException:
        print("No cookies")
        pass
    print("You have not yet logged into your last.fm account!")
    username = input("Type in your Last.fm username")
    password = input("Type in your Last.fm password")
    driver.find_element("id", "id_username_or_email").send_keys(username)
    driver.find_element("id", "id_password").send_keys(password)
    enterDiv = driver.find_element(By.CLASS_NAME, "form-submit")
    enter = enterDiv.find_element(By.TAG_NAME, "button")
    enter.click()

driver.implicitly_wait(5)
if(not driver.current_url.endswith("/user/" + username)):
    print("Something went wrong, please try again.")
else :
    driver.get("https://www.last.fm/home")


print('Hello')