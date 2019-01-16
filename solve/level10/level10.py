a = [1, 11, 21, 1211, 111221]
cnt = 1
addstr = ''

while(len(a) != 31):
    end = str(a[-1])
    for i in range(len(end)):
        if(i+1 < len(end) and end[i]==end[i+1]):
            cnt += 1
        else:
            addstr += str(cnt) + end[i]
            cnt = 1
    a.append(int(addstr))
    addstr = ''

print(len(str(a[-1])))
