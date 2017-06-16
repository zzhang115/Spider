from bs4 import BeautifulSoup
import requests, time

knewurl = 'https://knewone.com/discover?page='

def getDataFromPage(url, nth):
    webData = requests.get(url)
    soup = BeautifulSoup(webData.text, 'lxml')
    titles = soup.select('section.content > h4.title > a')
    images = soup.select('a.cover-inner > img')
    links = soup.select('section.content > h4.title > a')

    print("\n%dth page:" %(nth))
    for title, image, link in zip(titles, images, links):
        info = {
            'title' : title.get('title'),
            'img' : image.get('src'),
            'link' : link.get('href')
        }
        print(info)

def getMoreDataFromPage(start, end):
    for i in range(start, end):
        getDataFromPage(knewurl + str(i), i)
        time.sleep(1)

getMoreDataFromPage(1, 11)