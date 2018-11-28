import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
for page in range(1,39):
 my_url = "https://stackoverflow.com/jobs"
 uClient = uReq(my_url)
 page_html = uClient.read()
 uClient.close()
 page_soup=soup(page_html,"html.parser")
 page_var=page_soup.findall("div",{"class":"-title"})
 for i in page_var:
    job_name =i.findall("a",{"class":"s-link s-link__visited"})
    skills_required =job_name[i].findall("a",{"class":"post-tag job-link no-tag-menu"})
    print(job_name.string, end="------------")
    print(skills_required.string, end=" ")
    print("\n")