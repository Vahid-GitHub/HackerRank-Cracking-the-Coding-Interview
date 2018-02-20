#!/bin/python

import sys, heapq

def bisecSort(a):
    if (len(a) == 1):
        return(a)
    en = a.pop()
    l = 0
    h = len(a) - 1
    i = (l + h) // 2
    if (en <= a[l]):
        a = [en] + a
        return(a)
    if (en >= a[h]):
        a = a + [en]
        return(a)
    while ((h - l) > 1):
        if (en < a[i]):
            h = i
        else:
            l = i
        i = (l + h) // 2
    a = a[0:h] + [en] + a[h:]
    return(a)

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    a = bisecSort(a)
    if (len(a)%2 == 1):
        print("%.1f" % a[len(a)//2])
    else:
        print("%.1f" % (0.5 * (a[len(a)//2 - 1] + a[len(a)//2])))
