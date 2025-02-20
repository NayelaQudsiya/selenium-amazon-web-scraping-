from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to be found


query = "laptop"
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=36REPC42ZM5VI&sprefix=laptop%2Caps%2C345&ref=nb_sb_noss_2")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem.text)

# print(elem.get_attribute("outerHTML"))
# print(elem.text)

time.sleep(6)

driver.close()
