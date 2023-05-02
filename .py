import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

def scrape_job_listings(job_title, location, salary_threshold):
    base_url = "https://www.indeed.com"
    search_url = f"{base_url}/jobs?q={job_title}&l={location}&sort=date"
    jobs = []

    while search_url:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")

        job_cards = soup.find_all("div", class_="jobsearch-SerpJobCard")

        for card in job_cards:
            title_element = card.find("a", class_="jobtitle")
            if not title_element:
                continue

            title = title_element.text.strip()
            link = base_url + title_element["href"]
            date_posted = card.find("span", class_="date").text.strip()

            salary_element = card.find("span", class_="salaryText")
            if salary_element:
                salary = salary_element.text.strip()
                if salary_meets_threshold(salary, salary_threshold):
                    jobs.append({"job_name": title, "link_to_apply": link, "date_posted": date_posted})

        next_page = soup.find("a", {"aria-label": "Next"})
        search_url = base_url + next_page["href"] if next_page else None

    return jobs

def salary_meets_threshold(salary_text, threshold):
    # Add your logic here to compare salary_text with the threshold
    # You can use regex or string manipulation to extract salary values
    return True

job_titles = [
    "Software Engineer",
    "Software Developer",
    "Data Analyst",
    "Backend Engineer",
    "Django Developer",
    "Python Developer",
]

location = "United States"
salary_threshold = 90000

all_jobs = []

for title in job_titles:
    jobs = scrape_job_listings(title, location, salary_threshold)
    all_jobs.extend(jobs)

df = pd.DataFrame(all_jobs)
df.to_csv("high_paying_jobs.csv", index=False)
