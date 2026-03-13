from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
wait = WebDriverWait(browser,30)

website_url = "https://www.linkedin.com/signup"
browser.get(website_url)

email_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "input__input")))
email_box.send_keys("sindhiaazi110@gmail.com")

password_box = wait.until(EC.presence_of_element_located((By.ID , "password")))
password_box.send_keys("Aazar_is_Amazing@gmail.com")

login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME , "join-form__form-body-submit-button")))
login_button.click()

first_name = wait.until(EC.element_to_be_clickable((By.ID , "first-name")))
first_name.send_keys("Aazi")

last_name = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
last_name.send_keys("Jatoi")

continue_button = wait.until(EC.element_to_be_clickable((By.ID , "join-form-submit")))
continue_button.click()

input("Enter to quit")
browser.quit()
