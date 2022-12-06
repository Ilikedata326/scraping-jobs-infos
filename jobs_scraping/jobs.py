from bs4 import BeautifulSoup
import requests
import csv, time 


def findJobs():
    with open("jobs.csv", 'w',encoding="utf8", newline="") as file:
        write = csv.writer(file)
        header =  ["Company", "Skills", "Description", "Publish Date", "Experience", "Location"]
        write.writerow(header)

        # Get links of first 10 pages.
        links = []
        for page in range(1,11):
            url_base = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence="
            url_page = url_base + str(page)
            links.append(url_page) 

        for url in links:
            request = requests.get(url)
            soup = BeautifulSoup(request.content, "lxml")
            jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
            #print(jobs)
        
            for job in jobs:
                company = job.find("h3", class_="joblist-comp-name").text.replace("\r", "").replace("\n", "")
                skills = job.find("span", class_="srp-skills").text.replace("\r", "").replace("\n", "")
                description = job.find("ul", class_="top-jd-dtl clearfix").text.replace("\n", "")
                publish_date = job.find("span", class_="sim-posted").span.text.replace("\n", "")
                experience = job.find("ul", class_="top-jd-dtl clearfix").li.text.replace("\n", "")
                location = job.find("ul", class_="top-jd-dtl clearfix").span.text.replace("\n", "")
                #more_info
                infos = [company, skills, description, publish_date, experience, location]
                write.writerow(infos)       

# To execute programme every 10 minutes.
if __name__== '__main__':
    while True:
        findJobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)




