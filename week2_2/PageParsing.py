import pymongo
import requests
from bs4 import BeautifulSoup
from week2_2.ChannelExtract import getChannelURLS

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']
startUrl = 'http://sh.58.com/sale.shtml'

def getLinksFrom(channel, page, seller = 0):
    while 1:
        page = page + 1
        url= '{}pn{}/'.format(channel, str(page))
        # print(url)
        webData = requests.get(url)
        soup = BeautifulSoup(webData.text, 'lxml')
        # print(soup)
        isNoLongerExist = '404' in soup.find('link', type="text/css").get('href').split('/')[-1]
        if not isNoLongerExist:
            if soup.find('td', 't'):
                for link in soup.select('td.t > a.t'):
                    tmp = str(link.get('href'))
                    if tmp.startswith('http://z'):
                        itemLink = tmp.split('?')[0]
                    else:
                        continue
                    print(itemLink)
                    # url_list.insert_one({'url':itemLink})
                    getItemInfo(itemLink)
            else:
                print('exceed its total number of pages')
                break
        else:
            print("404 page")

def getItemInfo(url):
    webData = requests.get(url)
    soup = BeautifulSoup(webData.text, 'lxml')
    #title = soup.title.text #get page title
    itemTitle = soup.select('h1.info_titile')[0].text if soup.find_all('h1', 'info_titile') else None
    seller= soup.select('p.personal_name')[0].text if soup.find_all('p', 'personal_name') else None
    lookTime = soup.select('span.look_time')[0].text if soup.find_all('span', 'look_time') else None
    price = '￥' + soup.select('span.price_now > i')[0].text if soup.find_all('span', 'price_now') else None
    # item_info.insert_one({'title':itemTitle, 'seller':seller, 'lookTime':lookTime, 'price':price})
    print('title:%s seller:%s lookTime:%s price:%s' %(itemTitle, seller, lookTime, price))

def displayItemInMongoDB():
    for item in url_list.find():
        print(item)

# getLinksFrom('http://sh.58.com/diannao', 150, seller = 0)
# displayItemInMongoDB()
# getLinksFrom('http://bj.58.com/shouji/24605954621114x.shtml', 10 ,seller = 0)
# getItemInfo('http://zhuanzhuan.58.com/detail/865447324715352070z.shtml')
if __name__ == '__main__':
    urls = getChannelURLS(startUrl)
    for url in urls:
        getLinksFrom(url, 0)
