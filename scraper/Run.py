from LinkedinWebscraper import *

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

search("Rohin Sood")
print("----SEARCHED-----")

profileCount = resultCount()

profile(names, links, profileCount)
print("----GOT PROFILE & NAME LISTS-----")

information(locations, currentPos, experience, education, profileCount)
print(locations)
print(currentPos)
print(experience)
print(education)