import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']
startUrl = 'http://sh.58.com/sale.shtml'
i = 0

# http://cn-proxy.com/
# proxy_list = [
#     'http://117.177.250.151:8081',
#     'http://111.85.219.250:3129',
#     'http://122.70.183.138:8118',
#     ]
# proxy_ip = random.choice(proxy_list) # 随机获取代理ip
# proxies = {'http': proxy_ip}
# we can generate random IP to get page to solve restriction problem

# judge if page status is 404

def getLinksFrom(channel, page, seller = 0):
    url= '{}pn{}/'.format(channel, str(page))
    # print(url)
    try:
        webData = requests.get(url) # if webData.status_code == 404
        soup = BeautifulSoup(webData.text, 'lxml')
        isNoLongerExist = '404' in soup.find('link', type="text/css").get('href').split('/')[-1]
        if not isNoLongerExist:
            if soup.find('td', 't'):
                links = soup.select('td.t > a.t') if soup.find_all('td', 't') else None
                for link in links:
                    tmp = str(link.get('href'))
                    if tmp.startswith('http://z'):
                        itemLink = tmp.split('?')[0]
                    else:
                        continue
                    # print(itemLink)
                    url_list.insert_one({'url':itemLink})
                    getItemInfo(itemLink)
            else:
                print('exceed its total number of pages')
        else:
            print("404 page")
    except :
        print(url, " ConnectionError!")

def getItemInfo(url): # we can use len function to count how many items on current page
    try:
        webData = requests.get(url)
        soup = BeautifulSoup(webData.text, 'lxml')
        #title = soup.title.text #get page title
        isNoLongerExist = '404' in soup.find('h1').getText().split('/')[0]
        if isNoLongerExist:
            print("404 NotFound!")
            return
        itemTitle = soup.select('h1.info_titile')[0].text if soup.find_all('h1', 'info_titile') else None
        seller= soup.select('p.personal_name')[0].text if soup.find_all('p', 'personal_name') else None
        lookTime = soup.select('span.look_time')[0].text if soup.find_all('span', 'look_time') else None
        price = '￥' + soup.select('span.price_now > i')[0].text if soup.find_all('span', 'price_now') else None
        item_info.insert_one({'title':itemTitle, 'seller':seller, 'lookTime':lookTime, 'price':price})
        # print('title:%s seller:%s lookTime:%s price:%s' %(itemTitle, seller, lookTime, price))
    except :
        print(url, " ConnectionError!")

def displayItemInMongoDB():
    global i
    for item in url_list.find().limit(300):
    # for item in url_list.find():
        print(i,': ',item)
        i = i + 1
# displayItemInMongoDB()
# getLinksFrom('http://sh.58.com/diannao', 150, seller = 0)
# displayItemInMongoDB()
# getLinksFrom('http://bj.58.com/shouji/24605954621114x.shtml', 10 ,seller = 0)
# getItemInfo('/detail/846641854707843076z.shtml')
