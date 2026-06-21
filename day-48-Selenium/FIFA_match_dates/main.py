from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox()
driver.get("https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums?os=wtmb5utkcxk5&ref=app")



wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h4.ff-text-blue-dark")))
dates = driver.find_elements(By.CSS_SELECTOR, "h4.ff-text-blue-dark.article-section_headings__iQUD7")
for date in dates:
    data = date.text
    print(data)
