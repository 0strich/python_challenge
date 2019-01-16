f = open('./big.txt','r')

string = ''
result = ''
comp = '011101110'

for i in f:
    # translate big to low
    for j in i:
        if(j.islower()):
            string += '0'
        else:
            string += '1'
    if(string.find(comp) != -1):
        result += i[string.find(comp)+4]
    string = ''

print(result)

