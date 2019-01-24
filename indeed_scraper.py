import requests
from bs4 import BeautifulSoup
from job import *


class IndeedScraper:
    def __init__(self, jobType, location):
        self.__numPages = 3
        self.__jobType = jobType
        self.__location = location
        self.__baseUrl = self.__generateURL()

    def getJobType(self):
        return self.__jobType

    def getLocation(self):
        return self.__location

    def getJobs(self):  # returns a list of list of job
        pageNumber = 0
        url = self.__baseUrl + str(pageNumber)
        jobs = []

        for page in range(self.__numPages):
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            resultsCol = soup.find(id="resultsCol")
            results = resultsCol.find_all(class_="result")

            for result in results:
                linkContainer = result.find('a')
                title = self.__removeExtraSpaces(linkContainer.text)
                company = self.__removeExtraSpaces(result.find(class_="company").text)
                link = "https://www.indeed.ca"
                link += self.__removeExtraSpaces(linkContainer.attrs['href'])

                postingPage = requests.get(link)
                postingSoup = BeautifulSoup(postingPage.content, 'html.parser')
                description = postingSoup.find(class_="jobsearch-JobComponent-description").text

                job = Job(title, company, description, link)
                jobs.append(job)

            pageNumber += 20
            url = self.__baseUrl + str(pageNumber)

        return jobs

    def sortJobs(self, list):
        less = []
        equal = []
        greater = []

        if len(list) > 1:
            pivot = list[0]
            for x in list:
                if x.getNumMatchingSkills() < pivot.getNumMatchingSkills():
                    less.append(x)
                if x.getNumMatchingSkills() == pivot.getNumMatchingSkills():
                    equal.append(x)
                if x.getNumMatchingSkills() > pivot.getNumMatchingSkills():
                    greater.append(x)

            return self.sortJobs(greater) + equal + self.sortJobs(less)
        else:
            return list


    # private methods

    def __generateURL(self):
        url = "https://www.indeed.ca/jobs?q="
        url += self.__jobType.replace(' ', '+')
        url += "&l="
        url += self.__location
        url += "%2C+ON&start="
        return url

    def __removeExtraSpaces(self, string):
        string = string.lstrip()
        string = string.rstrip()
        return string

    def __urlExists(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            return True
        else:
            return False
