import urllib
import re

r = re.compile(r'href="(http://www.cnpythoner.com/.*?)"')


def get_urls_from_inside_url(url):
    try:
        opener = urllib.urlopen(url)
        contents = opener.read()
        g = r.finditer(contents)
        opener.close()
        return g
    except:
        print("Exception happen")
        return []

def get_url(url, data_cache, i):
    groups = get_urls_from_inside_url(url)
    for sub in groups:
        url = sub.group(1)
        # url = sub.group()[0]
        if url not in data_cache:
            i +=1
            data_cache.append(url)
        else:
            continue
        print("%d:%s" %(i, url))
        get_url(url, data_cache, i)

data_cache = []
get_url("http://www.cnpythoner.com/", data_cache, 0)
