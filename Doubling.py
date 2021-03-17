n,k = map(int,input().split())
a = list(map(lambda x: int(x)-1,input().split()))
a = {i:v for i,v in enumerate(a)}
doubling = [[-1] * n for i in range(k.bit_length())]
for key,val in a.items():
    doubling[0][key] = val
for i in range(1,k.bit_length()):
    for key in range(n):
        doubling[i][key] = doubling[i-1][doubling[i-1][key]]
ans = 0
for i in range(k.bit_length()):
    if 1 << i & k:
        ans = doubling[i][ans]
print(ans + 1)