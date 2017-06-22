import pymongo

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']

test = client['test']
testlist = test['testlist']

# newtongcheng = client['newtongcheng']
# newUrlList = newtongcheng['url_list']
# newItemInfo = newtongcheng['item_info']

# i = 0
# def displayItemInMongoDB():
#     # for item in url_list.find().limit(300):
#     global i
#     for item in url_list.find():
#         print(i,': ',item)
#         i = i + 1
# # displayItemInMongoDB()
# urls0 = item_info.find().count()
# print(urls0)
# for url in urls:
#     print(url)
# def testListInMongoDB():

# testlist.insert_one({'title': 1, 'value' : 'a'})
# testlist.insert_one({'title': 2, 'value' : 'a'})
# testlist.insert_one({'title': 3, 'value' : 'a'})
# testlist.insert_one({'title': 1, 'value' : 'a'})
# infos = []
# for item in item_info.find():
#     info = {
#         'title' : item['title'],
#         'price' : item['price'],
#         'seller' : item['seller'],
#         'lookTime' : item['lookTime']
#     }
#     if info not in infos:
#         infos.append(info)
# print(len(infos))








