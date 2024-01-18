from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os.path

def login_with_input() :
    try: 
        cookieBarIsPresent = driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookieBarIsPresent.click()
        # print("found")
    except NoSuchElementException:
        # print("No cookies")
        pass
    print("You have not yet logged into your last.fm account!")
    print("Type in your Last.fm username:")
    username = input("")
    print("Type in your Last.fm password:")
    password = input("")
    driver.find_element("id", "id_username_or_email").send_keys(username)
    driver.find_element("id", "id_password").send_keys(password)

    enterDiv = driver.find_element(By.CLASS_NAME, "form-submit")
    enter = enterDiv.find_element(By.TAG_NAME, "button")
    enter.click()


def handle_login_route() :
    global typeChoice
    global customArtist
    global recArtist
    global path
    recType = "All"
    if(customArtist):
        recType = recArtist
    if(not "/user/" in driver.current_url):
        print("Something went wrong, please try again.")
        driver.quit()
    else :
        if(int(typeChoice) == 1):
            driver.get("https://www.last.fm/home/tracks")
            path = "./" + recType +"_New_Recommended_Tracks.csv"
        elif(int(typeChoice) == 2):
            driver.get("https://www.last.fm/home/artists")
            path = "./" + recType + "_New_Recommended_Artists.csv"
        elif(int(typeChoice) == 3):
            driver.get("https://www.last.fm/home/albums")
            path = "./"+ recType + "_New_Recommended_Albums.csv"
    hasLoggedIn = True

def handle_rec_items(itemList):
    global path
    global typeChoice
    global customArtist
    global recArtist
    fileExists = os.path.isfile(path)
    with open(path, "a+", encoding="utf-8") as f:
        if(not fileExists):
            if(int(typeChoice) == 1):
                f.write("Song Name,Artist,Context\n")
            elif(int(typeChoice) == 2):
                f.write("Artist,Context\n")
            elif(int(typeChoice) == 3):
                f.write("Album Name,Artist,Context\n")
        for element in itemList :
            if(int(typeChoice) == 1 or int(typeChoice) == 3):
                if(int(typeChoice) == 1):
                    elemName = element[0][0:-7].replace(",", ";")
                else: 
                    elemName = element[0]
                elemArtist = element[1]
                context = element[2].replace(",", ";")
                fullName = elemName + "," + elemArtist
                f.seek(0)
                if (fullName not in f.read()) and ("You have scrobbled" not in context):
                    if(customArtist):
                        if(recArtist in context):
                            print("Added:\n" + elemName + " By " + elemArtist)
                            f.write(elemName + ",")
                            f.write(elemArtist + ',')
                            f.write(context + '\n')
                    else:
                        print("Added:\n" + elemName + " By " + elemArtist)
                        f.write(elemName + ",")
                        f.write(elemArtist + ',')
                        f.write(context + '\n')
            else:
                elemArtist = element[0]
                context = element[1].replace(",", ";")
                f.seek(0)
                if (elemArtist not in f.read()) and ("You have scrobbled" not in context):
                    if(customArtist):
                        if(recArtist in context):
                            print("Added:\n" + elemArtist)
                            f.write(elemArtist + ',')
                            f.write(context + '\n')
                    else:
                        print("Added:\n" + elemArtist)
                        f.write(elemArtist + ',')
                        f.write(context + '\n')


def get_recommended_items(recElement) :
    dividedInfoList = []
    for element in recElement:
        infoList = []
        try:
            titleContainer = element.find_element(By.CLASS_NAME, "recs-feed-title").text
            infoList.append(titleContainer)
            if(int(typeChoice) == 1 or int(typeChoice) == 3):
                artistContainer = element.find_element(By.CLASS_NAME, "recs-feed-description")
                artist = artistContainer.find_element(By.TAG_NAME, "a").text
                infoList.append(artist)
            context = element.find_element(By.CLASS_NAME, "context").text
            infoList.append(context)
        except NoSuchElementException:
            print("!Ad Element exception Caught!")
            pass
        if(len(infoList) > 0):
            dividedInfoList.append(infoList)
    return dividedInfoList


typeChoice = 0
customArtist = False
recArtist = ""
path = ""

while(True):
    print("What is the type of the recommendations you would like to receive?\n1)Track\n2)Artist\n3)Album")
    typeChoice = input("")
    if(not typeChoice.isnumeric()):
        typeChoice = 0
        print("Please enter a number")
    elif(int(typeChoice) < 1 or int(typeChoice) > 3):
        typeChoice = 0
        print("Please enter a number between 1 and 3")
    else: 
        break


recChoice = 0
while(recChoice == 0):
    print("Would you like to receive 1)all recommendations 2)recommendations based on specific artist?")
    recChoice = input("")
    if(not recChoice.isnumeric()):
        recChoice = 0
        print("Please enter a number")
    elif(int(recChoice) < 1 or int(recChoice) > 2):
        recChoice = 0
        print("Please enter a number between 1 and 2")
    if(int(recChoice) == 2): 
        customArtist = True
        print("Please specify(only one) artist to find recommendations for:")
        recArtist = input()

service=Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


driver.get("https://www.last.fm/")
time.sleep(1)

if(not driver.current_url.endswith("/home")):
    driver.get("https://www.last.fm/login")
    time.sleep(5)
    login_with_input()

time.sleep(2)
handle_login_route()

recommendationListElement = driver.find_elements(By.CLASS_NAME, "recs-feed-item")
itemList = get_recommended_items(recommendationListElement)
handle_rec_items(itemList)

