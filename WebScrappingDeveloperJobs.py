from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

for page in range(1,38):
    my_url='https://stackoverflow.com/jobs?sort=i&pg='+str(page)
    uClient=ureq(my_url)
    page_html=uClient.read()
    uClient.close()

    page_soup=soup(page_html,"html.parser")
    job_summary=page_soup.findAll("div",{"class":"js-search-results flush-left"})

    for job in job_summary:
        job_title = job.findAll("a", {"class": "s-link s-link__visited"})
        job_skill = job.findAll("div", {"class": "mt12 -tags"})

    for i in range(len(job_skill)):
        print(i,end=">>")
        print(job_title[i].string, end="<-------->")
        skills = job_skill[i].findAll("a", {"class": "post-tag job-link no-tag-menu"})
        for skill in skills:
            print(skill.string,end=",")
        print("\n")
