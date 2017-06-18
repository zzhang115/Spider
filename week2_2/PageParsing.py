from bs4 import BeautifulSoup
import requests, time, pymongo

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']

def getLinksFrom(channel, page, seller = 0):
    url= '{}/pn{}/'.format(channel, str(page))
    webData = requests.get(url)
    soup = BeautifulSoup(webData.text, 'lxml')
    for link in soup.select('td.t > a.t'):
        tmp = str(link.get('href'))
        if tmp.startswith('http://z'):
            itemLink = tmp.split('?')[0]
        else:
            itemLink = tmp
        print(itemLink)
        url_list.insert_one({'url':itemLink})

def displayItemInMongoDB():
    for item in url_list.find():
        print(item)

# getLinksFrom('http://sh.58.com/diannao', '10', seller = 0)
# displayItemInMongoDB()