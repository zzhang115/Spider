import xlrd
import pymongo
import os
from string import punctuation

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
item_info = tongcheng['item_info']
xlsx1 = 'california.xls'
# for i in item_info.find():#.limit(300):
#     if i['price']:
#         price = i['price']
#         price = price[1 : len(price)]
#         print(price)
        # item_info.update({'_id' : i['_id']}, {'price' : price})
# for i in item_info.find().limit(300):
#     print(i)

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
info = {
    'city' : '',
    'population' : '',
    'violent crime' : '',
    'murder' : '',
    'rape revised' : '',
    'rape legacy' : '',
    'robbery' : '',
    'aggravated assault' : '',
    'property crime' : '',
    'burglary' : '',
    'larceny theft' : '',
    'motor vehicle theft' : '',
    'arson' : '',
}
def readDataFromXlrd():
    wb = xlrd.open_workbook(os.path.join('california.xls'))
    wb.sheet_names()
    # print(wb.sheet_names())
    sh = wb.sheet_by_name('13tbl8ca')
    row = 6
    col = 0
    file = open('output.txt', 'w')
    for row in range(6, sh.nrows - 2):
        for col in range(sh.ncols):
            data = sh.cell_value(row, col)
            print(row, ' ', data)

readDataFromXlrd()