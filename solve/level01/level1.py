from string import *

string = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb
gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu
ynnjw ml rfc spj.'''

before = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
after = before[2:] + before[:2]

rep = maketrans(before, after)
print(string.translate(rep))

print('map'.translate(rep))
