from multiprocessing import Pool
from week2_3.ChannelExtract import channelList
from week2_3.PageParsing import getLinksFrom

def getAllLinksFrom(channel):
    for page in range(1, 101):
        getLinksFrom(channel, page)

if __name__ == '__main__':
    pool = Pool(processes=8)# it can distribute resource depends on your PC automatically processor=4
    pool.map(getAllLinksFrom, channelList.split())
    # print(channelList.split()) # channelList just a
    # print(channelList)

# function map: get element from right argument and pass it into double function one by one
'''def double(x):
    return x * 2
print(list(map(double, [1,2,3,4,5])))
'''

