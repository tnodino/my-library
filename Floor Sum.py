def floor_sum(n, m, a, b):
    ret = 0
    while True:
        if a >= m:
            ret += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            ret += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m:
            break
        n = y_max // m
        b = y_max % m
        m, a = a, m
    return ret

t = int(input())
for i in range(t):
    n,m,a,b = map(int,input().split())
    print(floor_sum(n,m,a,b))