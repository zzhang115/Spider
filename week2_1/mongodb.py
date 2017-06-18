import pymongo

client = pymongo.MongoClient('localhost', 27017)
admin = client['admin'] # table name in mongodb
sheet_table= admin['sheel_tab']

# path = 'walden.txt'
# with open(path, 'r') as file:
#     lines = file.readlines()
#     for index, line in enumerate(lines):
#         data = {
#            'index' : index,
#             'line' : line,
#             'words' : len(line.split())
#         }
#         print(data)
#         sheet_lines.insert_one(data)
# for item in sheet_table.find({'words':0}): # query dict structure
#     print(item)
# for item in sheet_table.find(): # query dict structure
#     print(item['line'])
for item in sheet_table.find({'words':{'$lt':5}}): # query dict structure
    print(item)
