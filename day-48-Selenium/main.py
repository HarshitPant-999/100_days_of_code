from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
#driver.get("https://www.amazon.in/Pulsar-Motorbike-Motorcycle-booking-Ex-Showroom/dp/B0D83Z7N75/?_encoding=UTF8&pd_rd_w=xv6cM&content-id=amzn1.sym.db089ca4-ba16-462d-addd-b73ebac82eee&pf_rd_p=db089ca4-ba16-462d-addd-b73ebac82eee&pf_rd_r=9CMVMPFC6N0E68WNEZ4Z&pd_rd_wg=0p7Vd&pd_rd_r=0014dee9-dfb7-4cc1-aee6-2440d7177abe&ref_=pd_hp_d_btf_ls_gwc_pc_en4_&th=1")
driver.get("https://www.python.org")
#price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#print(price_rupee)
#search_bar = driver.find_element(By.NAME, value="q")
#print(f"The price is {price_rupee.text}")
#print(search_bar.tag_name)
#print(search_bar.get_attribute("placeholder"))

#button = driver.find_element(By.ID, value="submit")
#print(button.size)

#documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#print(documentation_link.get_attribute("href"))
#driver.close()
#driver.quit()
#bug_link = driver.find_elements(By.X-PATH, value="/html/body/div/footer/div[1]/div/ul/li[7]/ul/li[3]/a")
#print(nug_link.text)

#elements = driver.find_elements(By.CSS_SELECTOR, value=".shrubbery .menu li")
#for element in elements:
   # print(element.find_element(By.CSS_SELECTOR, value="time").get_attribute("datetime"))
   # print(element.find_element(By.CSS_SELECTOR, value="a").get_attribute("href"))

time_element = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
link_element = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(time_element)):
    events[n] = {
        "time": time_element[n].text,
        "name": link_element[n].text
    }

print(events)
#print(datetime)
#print(link_name)
#driver.close()

