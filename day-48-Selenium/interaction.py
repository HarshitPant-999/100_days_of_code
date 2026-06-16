from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")



article = driver.find_element(By.CSS_SELECTOR ,value="#articlecount li a")
print(article)
