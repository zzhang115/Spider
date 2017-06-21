import pymongo
from string import punctuation

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
item_info = tongcheng['item_info']
for i in item_info.find().limit(300):
    print(i)

# here is a example to replace dirty data with punctuation, area here is a list
# for i in item_info.find().limit(300):
#     if i['area']:
#         area = [i for i in i['area'] if i not in punctuation]
#     else:
#         area = 'Undefined'
#     print(area)