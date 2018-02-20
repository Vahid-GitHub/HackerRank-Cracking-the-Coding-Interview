#!/bin/python3

def countInversions(arr):
    iCount = 0
    arr, iCount = mergeSort(arr, 0)
    print(arr)
    return(iCount)

def mergeSort(a, iCount):
    La = len(a)
    if (La < 2):
        return((a, iCount))
    div = 2
    div2 = 1
    while (div <= La):
        for i in range(0, La, div):
            (a[i:(i + div)], temp2) = mergeSortLists(a[i:(i + div2)], a[(i + div2):(i + div)])
            iCount += temp2
        div2 = div
        div *= 2
    (a, temp2) = mergeSortLists(a[:div2], a[div2:])
    iCount += temp2
    return((a, iCount))
    
def mergeSortLists(a, b):
    if (b == []):
        return((a, 0))
    La = len(a)
    Lb = len(b)
    iCounter = 0
    aPointer = 0
    bPointer = 0
    c = [None] * (La + Lb)
    while ((aPointer < La) & (bPointer < Lb)):
        if (a[aPointer] <= b[bPointer]):
            c[aPointer + bPointer] = a[aPointer]
            aPointer += 1
        else:
            c[aPointer + bPointer] = b[bPointer]
            bPointer += 1
            iCounter += (La - aPointer)
    if (aPointer < La):
        c[(aPointer + bPointer):] = a[aPointer:]
    if (bPointer < Lb):
        c[(aPointer + bPointer):] = b[bPointer:]
    return((c, iCounter))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
