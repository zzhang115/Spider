from bs4 import BeautifulSoup
import os
path = './web/new_index.html'

with open(path, 'r') as f:
    Soup = BeautifulSoup(f.read(), 'lxml')
    titles = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > h3 > a')

    print (titles)

'''
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.rate > span
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
'''