from LinkedinWebscraper import *
from Excel import *

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

searchString, searchURL = search(searchStringParam="Computer Science UCR 2018")
print("----SEARCHED-----")

profileCount = resultCount()

profile(names, links, 5)
print("----GOT PROFILE & NAME LISTS-----")

information(currentCo, locations, currentPos, experience, education, profileCount)
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
exporting()
