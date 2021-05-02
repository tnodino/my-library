def f(p):
    ret = 0
    for i in range(n):
        ret += (p - x[i]) ** 2 + (c - y[i]) ** 2
    return ret

n,c = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]
x,y = [list(i) for i in zip(*l)]
l = -10**5-1
r = 10**5+1
while l < r - 0.0000000001:
    c1 = (r - l) / 3 + l
    c2 = (r - l) / 3 * 2 + l
    if f(c1) > f(c2):
        l = c1
    else:
        r = c2
print(f(r))