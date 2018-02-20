def lonely_integer(a):
    return([x for x in a if (a.count(x) == 1)][0])
