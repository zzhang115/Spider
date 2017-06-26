import pymongo

client = pymongo.MongoClient('localhost', 27017)
sechand = client['SHG']
sechand_info = sechand['SecondHandGoods']
print(sechand_info.find().count())