import pymongo

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']

test = client['test']
testlist = test['testlist']
i = 0
def displayItemInMongoDB():
    # for item in url_list.find().limit(300):
    global i
    for item in url_list.find():
        print(i,': ',item)
        i = i + 1
# displayItemInMongoDB()

# def testListInMongoDB():
# testlist.insert_one({'test' : "test1"})
# testlist.insert_one({'test' : "test1"})
# distinctCollection = testlist.distinct('test')
# for item in testlist.distinct('test'):
#     print(item)

# print(testlist.count())
# for item in testlist.find('test'):
#     if item not in distinctCollection:
#         print(item)
# testlist.delete_many()

cursor = test.coll.aggregate(
    [
        {"$group": {"_id": "$ID", "test": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
        {"$match": {"count": { "$gte": 2 }}}
    ]
)

response = []
for doc in cursor:
    print(doc)
    del doc["test"][0]
    for id in doc["test"]:
        response.append(id)
print(response)
test.coll.remove({"_id": {"$in": response}})











