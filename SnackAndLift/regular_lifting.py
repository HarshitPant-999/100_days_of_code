from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

ACCOUNT_EMAIL = "harahitpant999@gmail.com"
ACCOUNT_PASSWORD = "OPIUM_DISORDER_PHOTO"
GYM_URL = "https://appbrewery.github.io/gym/"

profile_dir = os.path.join(os.getcwd(), "firefox_profile")
os.makedirs(profile_dir, exist_ok=True)

options = webdriver.FirefoxOptions()
options.add_argument("-profile")
options.add_argument(profile_dir)

#DRIVER
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)
driver.get(GYM_URL)

login_button = driver.find_element(By.ID, value="login-button")
login_button.click()
Email = driver.find_element(By.ID, value="email-input")
Email.send_keys(ACCOUNT_EMAIL, Keys.ENTER)
Password = driver.find_element(By.ID, value="password-input")
Password.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

tuesday = driver.find_element(By.ID, value="book-button-yoga-2026-06-23-0700")
tuesday.click()

upcomings = driver.find_elements(By.CSS_SELECTOR, value=".Schedule_dayTitle__YBybs")
#for text in upcomings:
 #   day = text.text.split()[0]
 #   print(day)
#if day == "Tue,":
  #  button_tuesday = driver.find_element(By.ID , value="book-button-yoga-2026-06-23-0700")
 #   button_tuesday.click()

#find_elements(By.CLASS, value="ClassCard_bookButton__DMM1I ClassCard_available__qnHvf")


#for id in find_elements(By.CSS_SELECTOR, value="p[id^='class-time-']")
#    id.find_element(By.ID, value=)

#if "Tue" in day_title:
    



class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button.click()

            print(f"✓ Booked: {class_name} on {day_title}")
