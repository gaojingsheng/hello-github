import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.yicai.com/data/')
r.encoding='utf-8'
soup = BeautifulSoup(r.text,'html.parser')
for news in soup.select('.dl-item'):
    print "news.select('h3')"
for news in soup.select('.dl-item'):
    print(news.select('h3')[0])
for news in soup.select('.dl-item'):
    print(news.select('h3')[0].text)
for news in soup.select('.dl-item'):
    h3 = news.select('h3')[0].text
    a = news.select('a')[0]['href']
    h4 =news.select('h4')[0].text
    print(h4,h3,a) 

