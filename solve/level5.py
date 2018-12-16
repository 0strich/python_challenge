from pickle import *
from urllib2 import *

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
req = Request(url)
fo = urlopen(req)

with open('../peak.txt','w') as peak:
    peak.write(fo.read())

with open('../peak.txt','rb') as load_file:
        data = load(load_file)

list_len = len(data)
print(len(data))

fo.close()
