from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time , sleep


driver = webdriver.Firefox()
driver.get("https://ozh.github.io/cookieclicker/")

sleep(15)

english = driver.find_element(By.ID , value="langSelect-EN")
english.click()
sleep(10)

button = driver.find_element(By.ID , value="bigCookie")

while True:
    sleep(0.1)
    button.click()
if cookie_score > 105:
    driver.find_element(By.ID, value="grandma click button")
