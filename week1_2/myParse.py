from bs4 import BeautifulSoup
import os
path = './web/new_index.html'
infoList = []
with open(path, 'r') as f:
    Soup = BeautifulSoup(f, 'lxml')
    # title = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > h3 > a')
    # image = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')
    # rate= Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.rate > span')
    # description = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > p.description')
    # print (titles)
    # print (image)
    # print (title)
    # print (description)

    #get rid of its specific position and get all title like things
    # allTitle = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    # allImage = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')
    # allRate= Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.rate > span')
    # allDescription = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > p.description')
    # allMetadata = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > p.meta-info > span')
    allTitle = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    allImage = Soup.select('body > div.main-content > ul > li > img')
    allRate= Soup.select('body > div.main-content > ul > li > div.rate > span')
    allDescription = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    allMetadata = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')

    # print("allTitle:", allTitle)
    # print("meta:", allMetadata)
for title, image, rate, description, metadata in zip(allTitle, allImage, allRate, allDescription, allMetadata):
        info = {
            "title" : title.get_text(),
            "image" : image.get('src'), #src is one attribute in image selector
            "rate" : rate.get_text(),
            "description" : description.get_text(),
            "cate" : list(metadata.stripped_strings),
        }
        infoList.append(info)
for information in infoList:
   if float(information['rate']) >= 4:
       print(information['title'])

    # print(title.get_text())
    # print(image.get('src'))
    # print(rate.get_text())
    # print(description.get_text())
    # print(metadata.get_text())

