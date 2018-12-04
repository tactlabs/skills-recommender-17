from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from collections import Counter
import matplotlib.pyplot as plt

skills1=[]

for page in range(2,39):
    my_url='https://stackoverflow.com/jobs?sort=i&pg='+str(page)
    uClient=ureq(my_url)
    page_html=uClient.read()
    uClient.close()

    page_soup=soup(page_html,"html.parser")
    job_summary=page_soup.findAll("div",{"class":"js-search-results flush-left"})

    for job in job_summary:
        job_skill = job.findAll("div", {"class": "mt12 -tags"})

    for i in range(len(job_skill)):
        skills = job_skill[i].findAll("a", {"class": "post-tag job-link no-tag-menu"})
        for skill in skills:
            skills1.append(skill.string)

d1=dict(Counter(skills1))

d2={}
d1_sorted_keys = sorted(d1, key=d1.get, reverse=True)
for r in d1_sorted_keys:
    if d1[r]>=30:
        d2.update({r:d1[r]})
    else:
        break

plt.figure(figsize=(500, 5))  # width:40, height:3
plt.bar(range(len(d2)), d2.values(), align='edge', width=0.3)
plt.xticks(range(len(d2)), d2.keys())
plt.show()
