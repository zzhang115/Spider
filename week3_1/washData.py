import pymongo
from string import punctuation

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
item_info = tongcheng['item_info']
# for i in item_info.find():#.limit(300):
#     if i['price']:
#         price = i['price']
#         price = price[1 : len(price)]
#         print(price)
        # item_info.update({'_id' : i['_id']}, {'price' : price})
for i in item_info.find().limit(300):
    print(i)

# here is a example to replace dirty data with punctuation, area here is a list
# for i in item_info.find().limit(300):
#     if i['area']:
#         area = [i for i in i['area'] if i not in punctuation]
#     else:
#         area = 'Undefined'
#     print(area)
# test = client['test']
# testlist = test['testlist']
# for i in testlist.find():
#     testlist.update({'_id' : i['_id']}, {'value' : 'b'})