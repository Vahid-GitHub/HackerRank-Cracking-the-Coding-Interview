#!/bin/python

import sys, heapq

n = int(raw_input().strip())
a = []
minHeap = []
maxHeap = []
heapq.heapify(minHeap)
heapq.heapify(maxHeap)
ma = -1
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    if (a_t < ma):
        heapq.heappush(maxHeap, -a_t)
    else:
        heapq.heappush(minHeap, a_t)
    if ((len(maxHeap) - len(minHeap)) == 2):
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))
    if ((len(minHeap) - len(maxHeap)) == 2):
        heapq.heappush(maxHeap, -heapq.heappop(minHeap))
    if (len(maxHeap) > 0):
        ma = -maxHeap[0]
    if (len(minHeap) > 0):
        mi = minHeap[0]
    if (len(maxHeap) == len(minHeap)):
        median = 1.0 * (ma + mi) / 2
    elif (len(maxHeap) < len(minHeap)):
        median = mi
    else:
        median = ma
    print("%.1f" % median)
