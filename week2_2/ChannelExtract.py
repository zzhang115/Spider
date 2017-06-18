from bs4 import BeautifulSoup
import requests

startUrl = 'http://sh.58.com/sale.shtml?PGTID=0d100000-0000-2cf0-81c7-feb5ddd2f642&ClickID=7'
baseUrl = 'http://sh.58.com'
def getChannelURLS(url):
    webData = requests.get(url)
    soup = BeautifulSoup(webData.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        subUrl = baseUrl + link.get('href')
        print(subUrl)

getChannelURLS(startUrl)
