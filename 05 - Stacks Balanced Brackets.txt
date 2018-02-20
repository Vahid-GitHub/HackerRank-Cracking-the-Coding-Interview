def is_matched(expression):
    isMatched = True
    dic = {'{': 1, '}': 2, '[': 3, ']': 4, '(': 5, ')': 6}
    brac = []
    for s in expression:
        if (dic[s]%2 == 1):
            brac.append(dic[s])
        else:
            if (len(brac) == 0):
                isMatched = False
                break
            elif (brac.pop() != (dic[s] - 1)):
                isMatched = False
                break
    if (len(brac) != 0):
        isMatched = False
    return (isMatched)

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
