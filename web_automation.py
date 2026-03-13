from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()
wait = WebDriverWait(browser,30)

website_url = "https://realpython.github.io/fake-jobs/"
browser.get(website_url)

jobs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR , ".column.is-half")))
job_counter = 1

for job in jobs:

    job_title = job.find_element(By.TAG_NAME , "h2").text
    job_counter += 1

    company = job.find_element(By.TAG_NAME , "h3").text
    location = job.find_element(By.CSS_SELECTOR , ".location").text.strip()
    date = job.find_element(By.CSS_SELECTOR , ".is-small.has-text-grey").text.strip()

    print(f"{job_counter}. Job : {job_title}")
    print(f"Company : {company}")
    print(f"Location : {location}")
    print(f"Date : {date}")
    print()
    
print("No more jobs")

input("Press Enter to quit")
browser.quit()

print("---- Stoping Automation ----")
print("---- Browser Closed ----")