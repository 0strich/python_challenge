from urllib.request import Request, urlopen
from re import findall

num = '12435'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=00000'
req = Request(url)
pr = ''

while(True):
    n_find = url.find(findall('\d+', url)[0])
    url = url[:n_find] + num
    req = Request(url)
    repeat = urlopen(req)
    r_file = repeat.read().decode()
    num = str(findall('\d+', r_file)[0])
    print(r_file)
repeat.close()
