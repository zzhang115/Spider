import xlrd
import pymongo
import os
from string import punctuation
import matplotlib.pyplot as plt
import numpy as np


client = pymongo.MongoClient('localhost', 27017)
crime = client['crime']
crime_info = crime['crime_info']
xlsx = ['california.xls', 'illinois.xls', 'new_york.xls', 'oregon.xls', 'tennessee.xls']

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
test = client['test']
testlist = test['testlist']
# testlist.insert_one({'title' : 'a', 'name' : 'abc', 'value' : 1})
# testlist.insert_one({'title' : 'a', 'name' : 'eddf', 'value' : 2})
# testlist.insert_one({'title' : 'a', 'name' : 'asfd', 'value' : 3})
# testlist.insert_one({'title' : 'a', 'name' : 'wwqre', 'value' : 4})
# testlist.insert_one({'title' : 'a', 'name' : 'qwer', 'value' : 5})
# testlist.insert_one({'title' : 'a', 'name' : 'hfd', 'value' : 6})

# for i in testlist.find():
    # testlist.update({'_id' : i['_id']}, {'title' : i['title'], 'name' : i['name'], 'value' : (int)(i['value']) + 10})
    # testlist.update({'_id' : i['_id']}, {'$set':{'value' : (int)(i['value']) + 10}})

data = []
def readDataFromXlrd(xlr):
    wb = xlrd.open_workbook(os.path.join(xlr))
    sh = wb.sheet_by_name(wb.sheet_names()[0])
    row = 6
    col = 0
    # file = open('output.txt', 'a')
    for row in range(6, sh.nrows - 2):
        # for col in range(sh.ncols):
            # info.keys()
        info = {
            'state' : xlr[0 : -4],
            'city': sh.cell_value(row, 0),
            'population': sh.cell_value(row, 1),
            'violent crime': sh.cell_value(row, 2),
            'murder': sh.cell_value(row, 3),
            'rape revised': sh.cell_value(row, 4),
            'rape legacy': sh.cell_value(row, 5),
            'robbery': sh.cell_value(row, 6),
            'aggravated assault': sh.cell_value(row, 7),
            'property crime': sh.cell_value(row, 8),
            'burglary': sh.cell_value(row, 9),
            'larceny theft': sh.cell_value(row, 10),
            'motor vehicle theft': sh.cell_value(row, 11),
            'arson': sh.cell_value(row, 12),
        }
        crime_info.insert_one(info)
        # data.append(info)
        # file.write(xlr[0 : -4]+' '+str(info.crimes())+'\n')
    # file.close()

def washData():
    for crime in crime_info.find():#.limit(200):
        if crime['rape revised'] == '':
            rapeRevised = 'None'
        else:
            rapeRevised = crime['rape revised']
        crime_info.update({'_id' : crime['_id']}, {'$set':{'rape revised' : rapeRevised}})

def watchData():
    for crime in crime_info.find():
        print(crime)

# for xlr in xlsx:
#     readDataFromXlrd(xlr)
# washData()
# watchData()
