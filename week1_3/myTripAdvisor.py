from bs4 import BeautifulSoup
import requests
import time

data = []
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
webdata = requests.get(url)
# print(webdata.text)
soup = BeautifulSoup(webdata.text, 'lxml')
# print(soup)
# titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div > div:nth-of-type(1) > a.poiTitle')#[target="_blank"]')
titles = soup.select('a.poiTitle')#[target="_blank"]')
# images = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > a:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > img:nth-of-type(1)')
images = soup.select('img[width="200"]')# set image width can eliminate other images we dont need
cates = soup.select('div.detail > div:nth-of-type(3)')# > div:nth-of-type(1)')# > div:nth-of-type(1) > div:nth-of-type(2) > div')
# print(titles)
# print(images)
# print(cates)

# for title in titles:
#     print(title.get_text())
# for image in images:
#     print(image.get('src'))
# for cate in cates:
#     print(cate.get_text())
for title, image, cate in zip(titles, images, cates):
    info = {
        "title:" : title.get_text(),
        "image:" : image.get('src'),
        "cate:" : cate.get_text(),
    }
    data.append(info)

for d in data:
    print(d)

