import xlrd
import pymongo
import os
from string import punctuation
import matplotlib.pyplot as plt
import numpy as np


client = pymongo.MongoClient('localhost', 27017)
djweb= client['djweb']
dj_info= djweb['djinfo1']

# for i in crime_info.find():#.limit(300):
#     if i['price']:
#         price = i['price']
#         price = price[1 : len(price)]
#         print(price)
        # crime_info.update({'_id' : i['_id']}, {'price' : price})
# for i in crime_info.find().limit(300):
#     print(i)

# here is a example to replace dirty data with punctuation, area here is a list
# for i in crime_info.find().limit(300):
#     if i['area']:
#         area = [i for i in i['area'] if i not in punctuation] # for this case ['SF', '-', 'USF'], delete middle punctuation
#     else:
#         area = 'Undefined'
#     print(area)
dj_info.insert_one({'title' : 'sky', 'des' : 'blue sky', 'score' : 5, 'tags' : ['blue sky', 'white cloud', 'hot sun']})
dj_info.insert_one({'title' : 'iphone', 'des' : 'smart phone', 'score' : 4.5, 'tags' : ['app store', 'smart siri', 'beautiful UI']})
dj_info.insert_one({'title' : 'bike', 'des' : 'pratical', 'score' : 5, 'tags' : ['helmet', 'chain', 'brake']})
dj_info.insert_one({'title' : 'computer', 'des' : 'great invention', 'score' : 5, 'tags' : ['ThinkPad T440p', 'Ubuntu', 'Python']})
# testlist.insert_one({'title' : 'a', 'name' : 'wwqre', 'value' : 4})
# testlist.insert_one({'title' : 'a', 'name' : 'qwer', 'value' : 5})
# testlist.insert_one({'title' : 'a', 'name' : 'hfd', 'value' : 6})


