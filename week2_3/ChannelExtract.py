from bs4 import BeautifulSoup
import requests

startUrl = 'http://sh.58.com/sale.shtml?PGTID=0d100000-0000-2cf0-81c7-feb5ddd2f642&ClickID=7'
baseUrl = 'http://sh.58.com'
urls = []
def getChannelURLS(url):
    webData = requests.get(url)
    soup = BeautifulSoup(webData.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        subUrl = baseUrl + link.get('href')
        # print(subUrl)
        urls.append(subUrl)
    return urls

channelList = '''
http://sh.58.com/xiangbao/
http://sh.58.com/zhubaoshipin/
http://sh.58.com/yuqi/
http://sh.58.com/tushu/
http://sh.58.com/tushubook/
http://sh.58.com/wenti/
http://sh.58.com/jianshenqixie/
http://sh.58.com/huju/
http://sh.58.com/qiulei/
http://sh.58.com/yueqi/
http://sh.58.com/chengren/
http://sh.58.com/nvyongpin/
http://sh.58.com/qinglvqingqu/
http://sh.58.com/qingquneiyi/
http://sh.58.com/chengren/
http://sh.58.com/xiaoyuan/
http://sh.58.com/ershouqiugou/
http://sh.58.com/tiaozao/
'''
getChannelURLS(startUrl)