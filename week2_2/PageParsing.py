from bs4 import BeautifulSoup
import requests, time, pymongo

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']

def getLinksFrom(channel, page, seller = 0):
    url= '{}/pn{}/'.format(channel, str(page))
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
                    itemLink = tmp
                print(itemLink)
                # url_list.insert_one({'url':itemLink})
        else:
            print('exceed its total number of pages')
            pass
    else:
        print("404 page")

def getItemInfo(url):
    webData = requests.get(url)
    soup = BeautifulSoup(webData.text, 'lxml')
    #title = soup.title.text #get page title
    itemTitle = soup.select('h1.info_titile')[0].text
    price = soup.select('span.price_now > i')[0].text
    print(itemTitle)
    print(price)

def displayItemInMongoDB():
    for item in url_list.find():
        print(item)

# getLinksFrom('http://sh.58.com/diannao', 150, seller = 0)
# displayItemInMongoDB()
# getLinksFrom('http://bj.58.com/shouji/24605954621114x.shtml', 10 ,seller = 0)
getItemInfo('http://zhuanzhuan.58.com/detail/865447324715352070z.shtml')