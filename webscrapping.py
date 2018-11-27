import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agent = UserAgent()
for page in range(1,39):
    main_url = 'https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab&sort=i&pg='+str(page)
    page = requests.get(main_url,headers={'user-agent':user_agent.chrome})
    soup = BeautifulSoup(page.content,'lxml')

    job_sum = soup.find_all("div", {"class": "js-search-results flush-left"})

    for job in job_sum:
        job_title = job.find_all("a", {"class": "s-link s-link__visited"})
        job_skill = job.find_all("div", {"class": "mt12 -tags"})

    for i in range(len(job_skill)):
        print(job_title[i].string, end="-------------------")
        skills = job_skill[i].find_all("a", {"class": "post-tag job-link no-tag-menu"})
        for skill in skills:
            print(skill.string, end=",")
        print("\n")
