f = open('./char.txt','r')
string = ''

for i in f:
    for j in i:
        if(j.isalpha()) : string += j

print(string)
