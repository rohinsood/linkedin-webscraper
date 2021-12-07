from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.add_argument("headless=false")
options.add_argument("window-size=1080, 720")
driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())
searchURL = ""
profileCount = 0
nameLi = []
linkLi = []
locationli = []
positionLi = []
expLi = []
eduLi = []

def isPresent(xpath):
    try: 
        driver.find_element_by_xpath(xpath)
        return True;
    except NoSuchElementException:
        return False;

def scrollTo(xpath):
    element = driver.find_element_by_xpath(xpath)

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()