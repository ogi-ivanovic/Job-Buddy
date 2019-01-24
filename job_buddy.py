from indeed_scraper import *

skills = []
print("Enter your skills ('done' when done):")
while True:
    skill = input()
    if skill == "done":
        break
    skills.append(skill)

print("Searching for jobs...")

open('scraped_jobs.txt', 'w').close()  # erases the contents of scraped_jobs.txt
scraper = IndeedScraper("software developer", "Ottawa")
jobs = scraper.getJobs()

# skills = ["Python", "C++", "Java", "SQL", "Javascript", "HTML", "CSS"]

for job in jobs:
    for skill in skills:
        if job.isSkill(skill):
            job.addMatchingSkill()

jobs = scraper.sortJobs(jobs)

header = "\n    Job Title                                    "
header += "Company                                           "
header += "# of Matching Skills\n\n"

jobNumber = 1
with open('scraped_jobs.txt', 'a') as scraped_jobs:
    scraped_jobs.write(header)
    for job in jobs:
        number = ""
        if len(str(jobNumber)) == 1:
            number = str(jobNumber) + " "
        else:
            number = str(jobNumber)
        if len(str(job.getDisplay2())) != 0:
            scraped_jobs.write(number + ". " + job.getDisplay2())
        jobNumber += 1

with open('scraped_jobs.txt', 'r') as scraped_jobs:
    print(scraped_jobs.read())

