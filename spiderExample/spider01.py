import urllib, re

r = re.compile(r'href="(http://www.cnpythoner.com.*?)"')

def getContentsFromUrl(url):
    try:
        opener = urllib.urlopen(url)
        contents = opener.read()
        writeToFile(contents, url)
        g = r.finditer(contents)
        opener.close()
        return g
    except:
        print "Exception happend"
        return []

def writeToFile(contents, url):
    filename = url.replace("http://", "")
    filename = filename.replace(".", "_")
    filename = filename.replace("/", "|")
    try:
        file  = open("spider1/%s.txt"%filename, "w")
        file.write(contents)
        file.close()
    except IOError:
        print "I/O exception"


def getUrlFromUrl(url, data_cache, i):
    groups = getContentsFromUrl(url)
    for sub in groups:
        url = sub.group(1)
        if url not in data_cache:
            data_cache.append(url)
            i += 1
            print i, ":", url
        else:
            continue
        getUrlFromUrl(url, data_cache, i)

data_cache = []
getUrlFromUrl("http://www.cnpythoner.com/", data_cache, 0)






