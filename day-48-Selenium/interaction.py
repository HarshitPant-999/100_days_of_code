from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")



article = driver.find_element(By.CSS_SELECTOR ,value="#articlecount li a")
#print(article)
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

