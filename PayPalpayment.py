from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators

#Open browser and navigate to home page
driver = webdriver.Firefox()
driver.get("https://www.deindeal.ch/fr/")

signInButton = driver.find_element_by_id(Locators.signInButton)
signInButton.click()

registerButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, Locators.registerButton)))
registerButton.click()

emailAddress = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, Locators.emailAddress)))
emailAddress.send_keys("test@testandrei.com")
passwordFiled = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, Locators.passwordFiled)))
passwordFiled.send_keys("123456")

selectCity = Select(driver.find_element_by_id(Locators.selectCity))
selectCity.select_by_value('geneve')

chooseGender = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, Locators.chooseGender)))
chooseGender.click()
submmitButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, Locators.submmitButton)))
submmitButton.click()