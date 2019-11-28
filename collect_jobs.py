import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver



def get_job_from_empoyment():
    jobs_store = []
    url = 'https://www.job.kg/vacancy/vbranch6'
    for page_number  in range(1,20):
        payload = {'sortby':2,'page':page_number}
        jobs_html = requests.get(url, params = payload)
        soup = BeautifulSoup(jobs_html.content, 'lxml')
        jobs = soup.find_all('li',{'class':'vvl-one vvl-ord- vvl-detaled- show- hide-note-comment clearfix'})
        for job in jobs:
            description = job.find('p',class_='clearfix m0').text if job.find('p',class_='clearfix m0') else None
            vacancy ={
            'company_name': job.find('span', class_='company-').text,
            'position': job.find('a',class_='title-').text,
            'description': re.sub('([\t,\n])','',description) if description else None,
            'salary': job.find('b', class_='salary-').text}
            jobs_store.append(vacancy)
            #print(vacancy)
    return jobs_store
