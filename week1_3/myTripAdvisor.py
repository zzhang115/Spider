from bs4 import BeautifulSoup
import requests
import time
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
webdata = requests.get(url)
# print(webdata.text)
soup = BeautifulSoup(webdata.text, 'lxml')
# print(soup)
titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div > div:nth-of-type(1) > a')#[target="_blank"]')
for t in titles:
    print(t.get_text())
# titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2)') > div:nth-of-type(1) > a')
# titles = soup.select('.top_attractions > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
# titles = soup.select('div.property_title > a[target="_blank"]')
print(titles)
# .top_attractions > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)
