def root(x):
    if r[x] < 0:
        return x
    else:
        r[x] = root(r[x])
        return r[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    if x != y:
        if r[x] > r[y]:
            x,y = y,x
        r[x] += r[y]
        r[y] = x

def size(x):
    return -r[root(x)]

n,q = map(int,input().split())
r = [-1] * n
for i in range(q):
    a,x,y = map(int,input().split())
    if a == 0:
        unite(x,y)
    else:
        if root(x) == root(y):
            print(1)
        else:
            print(0)