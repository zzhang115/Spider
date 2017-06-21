import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']

def displayItemInMongoDB():
    for item in url_list.find().limit(300):
    # for item in url_list.find():
        print(i,': ',item)
        i = i + 1
displayItemInMongoDB()