from urllib2 import *

rep = '12435'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=00000'
pr = ''

while(rep):
    url_str = str(filter(str.isdigit, url))
    url = url[:url.find(url_str)] + rep
    req = Request(url)
    fp = urlopen(req)
    pr = fp.read()
    rep = str(filter(str.isdigit, pr))
    print(pr)
fp.close()
