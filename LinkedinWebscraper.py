from Constants import *

"""
@function to log in :)
@param verif -> user inputed verif code
"""
def logIn (uname, pwd):
    username = driver.find_element_by_id("username")
    username.send_keys(uname)
    password = driver.find_element_by_id("password")
    password.send_keys(pwd)
    password.send_keys(Keys.RETURN)

"""
@function completes the user's 2fa if needed
@param verif -> user inputed verif code
"""
def twoFactor (verif):
    verifkey = driver.find_element_by_xpath('//*[@id="input__email_verification_pin"]')
    verifkey.send_keys(verif);
    verifkey.send_keys(Keys.RETURN)

"""
@function implements user-defined search string into url
@param searchString -> user-inputted search string
"""
def search (searchString):
    # Divide input string into words and append to list, then add each index of list to URL
    keywords = searchString.split()
    searchURL = "https://www.linkedin.com/search/results/people/?keywords="
    for i in range(len(keywords)):
        searchURL = searchURL + keywords[i] + "%20"
    driver.get(searchURL)

"""
@function gets name and profile link from the search page
"""
def profile():
    # gets # of results from the search
    profileCountStr = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]').text
    profileCount = int(profileCountStr.split()[0])
    
    # x is used to iterate over the profiles as there are only 10 profiles in 1 search page and i is the total amount of results which can be over 10
    x = 0
    # y is used to iterate over the different pages
    y = 1

    for i in range(profileCount):
        # scrolls to div of profile
        profileDiv = '//*[@id="main"]/div/div/div[2]/ul/li['+str(x+1)+']'
        scrollTo(profileDiv)

        # scrpares info & adds to list
        name = driver.find_element_by_xpath(profileDiv+'/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
        nameLi.append(name.text)
        profileURL = driver.find_element_by_xpath(profileDiv+'/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
        linkLi.append(profileURL.get_attribute("href"))

        x += 1

        # checks if the page is at it's max number of profiles (10), goes to the next page and repeats process
        if((0 == ((i+1)%10)) and (i != 0)):
            y += 1
            newPageURL = driver.current_url+"&page="+str(y)
            driver.get(newPageURL)
            x=0
        
def information():
    pass
    
# RUN CODE HERE
driver.get("https://www.linkedin.com/login?fromSignIn=true")
try:
    logIn('rs.rohinsood@gmail.com', '1861253d')
except NoSuchElementException:
    twoFactor(input("------------ENTER 2FA CODE------------\n"))
print("----LOGGED IN-----")

search("Anika Sood")
print("----SEARCHED-----")

profile()
print("----GOT PROFILE & NAME LISTS-----")

