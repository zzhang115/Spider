import pymongo

client = pymongo.MongoClient('admin', 'admin123')
admin = client['admin'] # table name in mongodb
sheet_lines = admin['sheel_lines']

path = ''
with open(path, 'r') as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        data = {
           'index' : index,
            'line' : line,
            'words' : len(line.split())
        }
        print(data)
