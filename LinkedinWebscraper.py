from sys import float_repr_style
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
    driver.find_element_by_xpath('//*[@id="global-nav"]')

"""
@function completes the user's 2fa if needed
@param verif -> user inputed verif code
"""
def twoFactor (verif):
    verifkey = driver.find_element_by_xpath('//*[@id="input__email_verification_pin"]')
    verifkey.send_keys(verif);
    verifkey.send_keys(Keys.RETURN)
    driver.find_element_by_xpath('//*[@id="global-nav"]')

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
@function get the # of results from search, used as a constant for later functions
"""
def resultCount():
    resultNumStr = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]').text
    resultNum = int(resultNumStr.split()[0])
    return resultNum

"""
@function gets name and profile link from the search page
@param nameList = names constant
@param linkList = links constant
@param resultNum = # of profiles
"""
def profile(nameList, linkList, resultNum):
    # x is used to iterate over the profiles as there are only 10 profiles in 1 search page and i is the total amount of results which can be over 10
    # so x can be reset every time it enters a new page in order to get to the list element while i continues past 10
    x = 0
    # y is used to iterate over the different pages
    y = 1

    for i in range(resultNum):
        # scrolls to div of profile
        profileDiv = '//*[@id="main"]/div/div/div[2]/ul/li['+str(x+1)+']'
        scrollTo(profileDiv)

        # scrpares info & adds to list
        name = driver.find_element_by_xpath(profileDiv+'/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
        nameList.append(name.text)
        profileURL = driver.find_element_by_xpath(profileDiv+'/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
        linkList.append(profileURL.get_attribute("href"))

        x += 1

        # checks if the page is at it's max number of profiles (10), goes to the next page and repeats process
        if((0 == ((i+1)%10)) and (i != 0)):
            y += 1
            newPageURL = driver.current_url+"&page="+str(y)
            driver.get(newPageURL)
            x=0


"""
@function scrapes info from each profile
@param resultNum = # of profiles
"""
def information(locList, posList, expList, eduList, resultNum):

    # profile iteration
    for i in range(resultNum):
        driver.get(links[i])

        location = driver.find_element_by_xpath('//*[@id="main"]/div/section/div[2]/div[2]/div[2]/span[1]')
        locList.append(location.text)

        position = driver.find_element_by_xpath('//*[@id="main"]/div/section/div[2]/div[2]/div/div[2]')
        posList.append(position.text)

        expElementList = driver.find_elements_by_xpath('//*[@id="experience-section"]/ul/li')

        print("LENGHT OF EXP: " + str(len(expElementList)))

        # experience iteration
        for z in range(len(expElementList)):
            expXPath = '//*[@id="experience-section"]/ul/li['+str(z+1)+']/section/div/div'
            scrollTo(expXPath)

            try:
                expTitle = driver.find_element_by_xpath(expXPath + '/a/div[2]/h3').text
            except NoSuchElementException:
                expTitle = noInfo + "Title of Experience"

            try:
                expCompany = driver.find_element_by_xpath(expXPath + '/a/div[2]/p[2]').text
            except NoSuchElementException:
                expCompany = noInfo + "Company of Experience"

            try:
                expDuration = driver.find_element_by_xpath(expXPath + '/a/div[2]/div/h4[2]/span[2]').text
            except NoSuchElementException:
                expDuration = noInfo + "Duration of Experience"

            expURLElement = driver.find_element_by_xpath(expXPath + "/a")
            expURL = "https://www.linkedin.com" + expURLElement.get_attribute("href")

            expList.append([expTitle, expCompany, expDuration, expURL])


        eduElementList = driver.find_elements_by_xpath('//*[@id="education-section"]/ul/li')
        print("EDU LEN: " + str(len(eduElementList)))

        for t in range(len(eduElementList)):
            eduXPath = '//*[@id="education-section"]/ul/li['+str(t+1)+']/div/div'
            scrollTo(eduXPath)

            try:
                eduInstitution = driver.find_element_by_xpath(eduXPath + '/a/div[2]/div/h3').text
            except NoSuchElementException:
                eduInstitution = noInfo + "Educational Instituion"

            try:
                eduDegree = driver.find_element_by_xpath(eduXPath + '/a/div[2]/div/p[1]/span[2]').text
            except NoSuchElementException:
                eduDegree = noInfo + "Education Degree"

            try:
                eduTitleNum = len(driver.find_elements_by_xpath(eduXPath + "/a/div[2]/div/p"))
                eduDuration = driver.find_element_by_xpath(eduXPath + '/a/div[2]/div/p['+str(eduTitleNum)+']/span[2]').text
            except NoSuchElementException:
                eduDuration = noInfo + "Duration of Education"

            eduURLElement = driver.find_element_by_xpath(eduXPath + "/a")
            eduURL = "https://www.linkedin.com" + eduURLElement.get_attribute("href")

            eduList.append([eduInstitution, eduDegree, eduDuration, eduURL])
            
    
# RUN CODE HERE
driver.get("https://www.linkedin.com/login?fromSignIn=true")
while True:
    try:
        logIn('rs.rohinsood@gmail.com', '1861253d')
        break
    except NoSuchElementException:
        try:
            twoFactor(input("------------ENTER 2FA CODE------------\n"))
            break
        except NoSuchElementException:
            continue

print("----LOGGED IN-----")

search("Anika Sood")
print("----SEARCHED-----")

print("PROFILE COUNT: " + str(profileCount))
profileCount = resultCount()
print("PROFILE COUNT UPDATED: " + str(profileCount))

profile(names, links, profileCount)
print("----GOT PROFILE & NAME LISTS-----")

information(locations, currentPos, experience, education, profileCount)
print(locations)
print(currentPos)
print(experience)
print(education)


