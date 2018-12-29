from pickle import *
from urllib.request import *

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
response = urlopen(url)

with open('../peak.txt','w') as peak:
    peak.write(response.read().decode())

with open('../peak.txt','rb') as load_file:
        data = load(load_file)

for i in data:
    for j in i:
        print(j[0] * j[1], end='')
    print('', end='\n')

