from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser,20)

website = "https://www.saucedemo.com"
browser.get(website)

username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
username_field.send_keys("standard_user")
time.sleep(1)

password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
password_field.send_keys("secret_sauce")
time.sleep(1)

login_button = wait.until(EC.element_to_be_clickable((By.ID , "login-button")))
login_button.click()
time.sleep(1)

item_container = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
print(f"Total Items : {len(item_container)}")

for item in item_container:
    
    item_name = item.find_element(By.CLASS_NAME , "inventory_item_name").text.strip()
    item_price = item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip()

    print(f"Item : {item_name}")
    print(f"Price : {item_price}")
    print()

input("press enter to stop the script")
browser.quit()
print("--- Browser Closed ---")