from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

def login_with_input() :
    global choice
    try: 
        cookieBarIsPresent = driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookieBarIsPresent.click()
        print("found")
    except NoSuchElementException:
        print("No cookies")
        pass
    print("You have not yet logged into your last.fm account!")
    print("Type in your Last.fm username:")
    username = input("")
    print("Type in your Last.fm password:")
    password = input("")
    driver.find_element("id", "id_username_or_email").send_keys(username)
    driver.find_element("id", "id_password").send_keys(password)
    while(True):
        print("What is the type of the recommendations you would like to receive?\n1)Track\n2)Artist\n3)Album")
        choice = input("")
        if(not choice.isnumeric()):
            choice = 0
            print("Please enter a number")
        elif(int(choice) < 1 or int(choice) > 3):
            choice = 0
            print("Please enter a number between 1 and 3")
        else: 
            break
    enterDiv = driver.find_element(By.CLASS_NAME, "form-submit")
    enter = enterDiv.find_element(By.TAG_NAME, "button")
    enter.click()

def check_login_success(number) :
    if(not "/user/" in driver.current_url):
        print("Something went wrong, please try again.")
        driver.quit()
    else :
        if(int(number) == 1):
            driver.get("https://www.last.fm/home/tracks")
        elif(int(number) == 2):
            driver.get("https://www.last.fm/home/artists")
        elif(int(number) == 3):
            driver.get("https://www.last.fm/home/albums")
    hasLoggedIn = True

# def check_element_for_class(element, attribute):

def get_recommended_items(recElement) :
    dividedInfoList = []
    for element in recElement:
        infoList = []
        try:
            titleContainer = element.find_element(By.CLASS_NAME, "recs-feed-title").text
            infoList.append(titleContainer)
            if(int(choice) == 1 or int(choice) == 3):
                artistContainer = element.find_element(By.CLASS_NAME, "recs-feed-description")
                artist = artistContainer.find_element(By.TAG_NAME, "a").text
                infoList.append(artist)
            context = element.find_element(By.CLASS_NAME, "context").text
            infoList.append(context)
        except NoSuchElementException:
            print("Error?")
            pass
        if(len(infoList) > 0):
            dividedInfoList.append(infoList)
    return dividedInfoList

service=Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


hasLoggedIn = False
choice = 0

driver.get("https://www.last.fm/")
driver.implicitly_wait(2)

if(driver.current_url.endswith("/home")):
    hasLoggedIn = true
else:
    driver.get("https://www.last.fm/login")
    time.sleep(6)
    login_with_input()

time.sleep(5)
check_login_success(choice)
print(choice)

recommendationListElement = driver.find_elements(By.CLASS_NAME, "recs-feed-item")
itemList = get_recommended_items(recommendationListElement)


for array in itemList:
    print(array)

