from selenium import webdriver
import os

ACCOUNT_EMAIL = "harahitpant999@gmail.com"
ACCOUNT_PASSWORD = "OPIUM_DISORDER_PHOTO"
GYM_URL = "https://appbrewery.github.io/gym/"

profile_dir = os.path.join(os.getcwd(), "firefox_profile")
os.makedirs(profile_dir, exist_ok=True)  # Firefox needs the dir to exist beforehand

options = webdriver.FirefoxOptions()
options.add_argument("-profile")
options.add_argument(profile_dir)


driver.get(GYM_URL)
