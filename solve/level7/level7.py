from PIL import Image
from re import findall

im = Image.open('./oxygen.png')
pix, size = im.load(), im.size
x, y = size[0], size[1]               # x = 629, y =  95
pix_lst = list()
extract = list()
mid_y = y / 2

for i in range(0, x, 7):
    pix_lst.append(pix[i, mid_y][2])

extract = ''.join([chr(i) for i in pix_lst])
extract = map(int, findall('\d+', extract))
Next_Key = ''.join([chr(i) for i in extract])
print(Next_Key)

im.close()
