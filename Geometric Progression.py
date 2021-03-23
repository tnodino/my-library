n = int(input())
z = [list(map(int,input().split())) for i in range(n)]
a,l = [list(i) for i in zip(*z[::-1])]
mod = int(input())
ans = 0
digit = 0
for i in range(n):
    # 等比数列の和 a = 初項、 r = 公比、初項から n 項までの和
    # (a * (r ^ n) - a) / (r - 1)
    # 今回の l[i] 項の長さは (1 ... (10 ^ len(a[i]) ^ (l[i] - 1)) なので
    # (10 ^ len(a[i])) ^ l[i] - 1
    m = len(str(a[i]))
    p = pow(10,m,mod)
    x = pow(p,l[i],mod) - 1
    y = p - 1
    # x / y = x * pow(y,mod-2,mod)
    z = a[i] * x * pow(y,mod-2,mod)
    ans += z * pow(10,digit,mod)
    ans %= mod
    digit += m * l[i]
print(ans)