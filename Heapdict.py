from collections import defaultdict
from heapq import heappop,heappush
import sys
readline = sys.stdin.readline

class HeapDict:
    def __init__(self):
        self.heap = []
        self.dic = defaultdict(int)

    def add(self,x):
        self.dic[x] += 1
        heappush(self.heap,x)

    def remove(self,x):
        self.dic[x] -= 1
        while self.heap:
            if self.dic[self.heap[0]] == 0:
                heappop(self.heap)
            else:
                break

    def getmin(self):
        return -self.heap[0]

B = 2 * (10 ** 5)
n,q = map(int,readline().split())
kind = [HeapDict() for i in range(B)]
child = []
for i in range(n):
    a,b = map(int,readline().split())
    b -= 1
    kind[b].add(-a)
    child.append([a,b])
maxset = HeapDict()
for i in range(B):
    if kind[i].heap:
        maxset.add(kind[i].getmin())
for i in range(q):
    c,d = map(int,readline().split())
    c -= 1
    d -= 1
    x,y = child[c]
    maxset.remove(kind[y].getmin())
    if kind[d].heap:
        maxset.remove(kind[d].getmin())
    kind[y].remove(-x)
    kind[d].add(-x)
    if kind[y].heap:
        maxset.add(kind[y].getmin())
    maxset.add(kind[d].getmin())
    print(maxset.heap[0])
    child[c] = [x,d]