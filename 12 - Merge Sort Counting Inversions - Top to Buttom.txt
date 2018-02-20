#!/bin/python3

import sys

def countInversions(arr):
    iCount = 0
    arr, iCount = mergeSort(arr, 0)
    return(iCount)

def mergeSort(a, iCount):
    La = len(a)
    if (La < 2):
        return((a, iCount))
    La2 = La // 2
    a1, iCount = mergeSort(a[:La2], iCount)
    b1, iCount = mergeSort(a[La2:], iCount)
    (c, iCount3) = mergeSortLists(a1, b1)
    iCount += iCount3
    return((c, iCount))
    
def mergeSortLists(a, b):
    a = list(a)
    b = list(b)
    La = len(a)
    Lb = len(b)
    iCounter = 0
    aPointer = 0
    bPointer = 0
    c = []
    while ((aPointer < La) & (bPointer < Lb)):
        if (a[aPointer] <= b[bPointer]):
            c.append(a[aPointer])
            aPointer += 1
        else:
            c.append(b[bPointer])
            bPointer += 1
            iCounter += (La - aPointer)
    c = c + a[aPointer:]
    c = c + b[bPointer:]
    return((c, iCounter))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
