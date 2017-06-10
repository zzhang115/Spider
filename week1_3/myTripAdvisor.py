from bs4 import BeautifulSoup
import requests
import time
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
webdata = requests.get(url)
# print(webdata.text)
soup = BeautifulSoup(webdata.text, 'lxml')
# print(soup)
# titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div > div:nth-of-type(1) > a.poiTitle')#[target="_blank"]')
titles = soup.select('a.poiTitle')#[target="_blank"]')
# images = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > a:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > img:nth-of-type(1)')
images = soup.select('img[width="200"]')# set image width can eliminate other images we dont need
print(titles)
print(images)

for title in titles:
    print(title.get_text())
for image in images:
    print(image.get('src'))
# titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2)') > div:nth-of-type(1) > a')
# .top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > a:nth-of-type(1)
