import os
import time
import requests
from bs4 import BeautifulSoup

url = "http://m.ctrip.com/html5/flight/swift/domestic/TYN/CAN/2017-08-20?SortByPrice=true#ctm_ref=fld_sr_9lp_sr_bn"
headers  = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Connection':'keep-alive'
}
def notify():
    while True:
        os.system("/usr/bin/canberra-gtk-play --id='bell'")
        time.sleep(1)

def getInfoFromPage(url):
    webData = requests.get(url, headers = headers)
    soup = BeautifulSoup(webData.text, 'lxml')
    print(soup)
    info = {
        'logo' : soup.select('td.logo'),#> div.clearfix > strong'),

    }
    print(info)
getInfoFromPage(url)

