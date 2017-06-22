import time
from week2_3.PageParsing import url_list
i = 0
while True:
    i = i + 1
    print(i, ' ', url_list.find().count())
    time.sleep(5)