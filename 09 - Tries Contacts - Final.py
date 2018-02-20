def add(dic, name):
    temp = dic
    for letter in name:
        temp.setdefault(letter, {'Frequency':0})
        temp[letter]['Frequency'] += 1
        temp = temp[letter]
    temp['End'] = None
def find(dic, name):
    subDic = dic
    for letter in name:
        if (subDic.has_key(letter)):
            subDic = subDic[letter]
        else:
            return(0)
    return(subDic['Frequency'])

names = dict()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if (op == 'add'):
        add(names, contact)
    elif (op == 'find'):
        print(find(names, contact))

