from selenium import webdriver
from Locators import Locators
import time

driver = webdriver.Firefox()
driver.get("https://www.deindeal.ch/fr/")
driver.find_element_by_id(Locators.foodDelivery).click()
time.sleep(5)
curretnURl = driver.current_url
assert curretnURl.find("restaurant") != -1
showRestaurant = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/button')
if showRestaurant.is_enabled():
    print("Element is enabled")
else:
    pass