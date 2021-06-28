from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests

from Locators import Locators
import time

#Open browser and navigate to home page
driver = webdriver.Firefox()
driver.get("https://www.deindeal.ch/fr/")

#Find "food delevery" and click the link
foodDelivery = driver.find_element_by_id(Locators.foodDelivery).click()
time.sleep(5)

#Get the current url, assert it and verify if the button that shows the restaurants is disabled
curretnURl = driver.current_url
assert curretnURl.find("restaurant") != -1
showRestaurant = driver.find_element_by_xpath(Locators.showRestaurant)
if showRestaurant.is_enabled():
    print("Element is enabled")
else:
    pass


#Enter the address for delivery and click sugestion

addressForDelivery = driver.find_element_by_xpath(Locators.addressForDelivery)
addressForDelivery.send_keys("Rue Emma-Kammacher 9")
suggestion = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, Locators.suggestion)))
actions = ActionChains(driver)
actions.move_to_element(suggestion)
actions.click(suggestion)
actions.perform()

#Click the right arrow to select "healthy" food category

rightFilterFoodArrow = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.rightFilterFoodArrow)))
rightFilterFoodArrow.click()
time.sleep(5)

#Select healthy food from filter
libanaisFood = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locators.libanaisFood)))
libanaisFood.click()
time.sleep((5))
#Close the pop-up
driver.switch_to.frame(Locators.marketingFrame)
closePopUpButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.closeButtonMarketingFrame)))
closePopUpButton.click()
time.sleep(3)

#Assert filter
filteredURL = driver.current_url
assert filteredURL.find("sortBy=fd_libanese") != -1

#Get list of ids
searchResults = driver.find_elements_by_css_selector(".SalesList__list")
print(searchResults)
for x in range(len(searchResults)):
    print(searchResults[x])

#Make the api call

def apiiCall():
    response = requests.get("https://testfoodios.herokuapp.com/food_city/geneve")
    print(response)
    assert response.status_code == 200

apiiCall()


