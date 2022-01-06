from Excel import *
from Scraper import *

driver.get("https://www.linkedin.com/login?fromSignIn=true")

# used for 2fa and incorrect passwords
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

searchString, searchURL = search(searchStringParam="Anika Sood")
print("----SEARCHED-----")

profileCount = resultCount()

profileCount = profile(names, links, 20)
print(links)
print("----GOT PROFILE & NAME LISTS-----")
  
information(currentCo, locations, currentPos, experience, education)
print(names)
print(links)
print(currentCo)
print(locations)
print(currentPos)
print(experience)
print(education)
print(searchString)
print(searchURL)
print(profileCount)

driver.close()

print("------Exporting------")
Excel.exporting(namesLi=names, linksLi=links, currentCoLi=currentCo, locationsLi=locations, currentPosLi=currentPos, experienceLi=experience, educationLi=education, profCount=profileCount, searchLink=searchURL)

print("-----Finished Exoprting-----")