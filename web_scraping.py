import requests
from bs4 import BeautifulSoup
import csv
with open("Jobs.csv" , "w" , newline="" , encoding="utf-8") as x:
    i = csv.writer(x)
    i.writerow(["Job","Company","Location","Date"])

    url = "https://realpython.github.io/fake-jobs/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text , "html.parser")

    jobs = soup.find_all("div" , class_="column is-half")
    print(f"Total Jobs : {len(jobs)}")
    job_counter = 1

    for job in jobs:

        job_title = job.find("h2" , class_="title is-5").text
        job_counter += 1

        company = job.find("h3" , class_="subtitle is-6 company").text
        location = job.find("p" , class_="location").text.strip()
        date = job.find('p' , class_="is-small has-text-grey").text.strip()

        print(f"{job_counter}. Job : {job_title}")
        print(f"Company : {company}")
        print(f"Location : {location}")
        print(f"Date : {date}")
        print()
        i.writerow([job_title,company,location,date])

    print("No More Jobs")
    print("--- Scraping Done ---")
