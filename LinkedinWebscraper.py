from os import name
from Constants import *

def logIn (uname, pwd):
    username = driver.find_element_by_id("username")
    username.send_keys(uname)
    password = driver.find_element_by_id("password")
    password.send_keys(pwd)
    password.send_keys(Keys.RETURN)

def twoFactor (verif):
    verifkey = driver.find_element_by_xpath('//*[@id="input__email_verification_pin"]')
    verifkey.send_keys(verif);
    verifkey.send_keys(Keys.RETURN)

def search (searchString):
    # Divide input string into words and append to list, then add each index of list to URL
    keywords = searchString.split()
    searchURL = "https://www.linkedin.com/search/results/people/?keywords="
    for i in range(len(keywords)):
        searchURL = searchURL + keywords[i] + "%20"
    driver.get(searchURL)

def getProfileList():
    profileCountStr = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]').text
    profileCount = int(profileCountStr.split()[0])
    
    for i in range(profileCount):
        profileDiv = "/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li["+str(i+1)+"]"
        scrollTo(profileDiv)

        name = driver.find_element_by_xpath(profileDiv+'/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
        nameLi.append(name.text)

        profileURL = driver.find_element_by_xpath(profileDiv+'/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
        profileURL.getAttribute("href")
        linkLi.append(profileURL)
        print(i+"\n")
    
    print(nameLi+"\n")
    print(linkLi+"\n")
        
    
    
# RUN CODE HERE
driver.get("https://www.linkedin.com/login?fromSignIn=true")
try:
    logIn('rs.rohinsood@gmail.com', '1861253d')
except NoSuchElementException:
    twoFactor(input("------------ENTER 2FA CODE------------\n"))
print("----LOGGED IN-----")

search("Anika Sood")
print("----SEARCHED-----")

getProfileList()
print("----GOT PROFILE & NAME LISTS-----")

