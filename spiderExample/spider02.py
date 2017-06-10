import urllib, re, threading, Queue

data_cache = []
r = re.compile(r'href="(http://www.cnpythoner.com.*?)"')
queue = Queue.Queue()
lock = threading.RLock()

def getContentsFromUrl():
    while True:
        # lock.acquire()
        url = queue.get()
        print url
        # lock.release()
        try:
            opener = urllib.urlopen(url)
            contents = opener.read()
            # writeToFile(contents, url)
            g = r.finditer(contents)
            opener.close()
            getUrlFromUrl(g)
        except:
            print "Exception happend"

def writeToFile(contents, url):
    filename = url.replace("http://", "")
    filename = filename.replace(".", "_")
    filename = filename.replace("/", "|")
    try:
        file  = open("spider2/%s.txt"%filename, "w")
        file.write(contents)
        file.close()
    except IOError:
        print "I/O exception"

def getUrlFromUrl(groups):
    lock.acquire()
    for sub in groups:
        url = sub.group(1)
        if url not in data_cache:
            data_cache.append(url)
            print "url:", url
            queue.put(url)
        else:
            continue
        # getUrlFromUrl(url, data_cache, i)
    lock.release()

queue.put("http://www.cnpythoner.com/")
# getContentsFromUrl()
threads = []
for i in range(1, 100):
    t = threading.Thread(target=getContentsFromUrl)
    t.start()
    threads.append(t)
for t in threads:
    t.join()

