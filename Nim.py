from math import sqrt
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(2,int(sqrt(n))+1):
    while n % i == 0:
        d[i] += 1
        n //= i
if n > 1:
    d[n] += 1
nim = 0
for i in d.values():
    nim ^= i
if nim:
    print('Alice')
else:
    print('Bob')