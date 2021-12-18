from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


s = Service(ChromeDriverManager().install())
options = Options()
# options.add_argument("--headless")  
options.add_argument("window-size=1080, 720")
driver = webdriver.Chrome(service=s, options=options)

searchURL = "https://www.linkedin.com/search/results/people/?keywords="
searchString = ""
profileCount = 0
noInfo = "No Info Found for: "

names = []
links = []
locations = []
currentPos = []
experience = []
education = []
currentCo = []

def scrollTo(xpath):
    element = driver.find_element_by_xpath(xpath)

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
