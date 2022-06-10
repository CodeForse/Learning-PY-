import requests
from bs4 import BeautifulSoup 
import random
#your parameters:
first_page=1
border_page=5
sample_size=4

file = open('news.txt', 'w')
file.truncate()
total_for_range = []
for p in range(first_page,border_page):
     url=f"https://tengrinews.kz/kazakhstan_news/page/{p}"
     r=requests.get(url)
     soup= BeautifulSoup(r.text, 'lxml')
     total_titals_on_page=soup.find('div', class_='tn-article-grid').findAll('span',class_='tn-hidden')
     for i in total_titals_on_page:
      total_for_range.append(i.text)
k=1
for i in random.sample(total_for_range,sample_size):
  print(str(k)+') ')
  k=k+1
  print(i)
  file.write(i+ '\n')

file.close()