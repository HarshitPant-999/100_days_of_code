from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name = driver.find_element(By.NAME , value="fName")
first_name.send_keys("harsh" ,Keys.ENTER)

second_name = driver.find_element(By.NAME, value="lName")
second_name.send_keys("pant", Keys.ENTER)

email = driver.find_element(By.NAME, value="email")
email.send_keys("harahitpant999@gmail.com", Keys.ENTER)
