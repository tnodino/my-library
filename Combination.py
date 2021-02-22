def cmb(n,r):
    if (r < 0) or (n < r):
        return 0
    r = min(r,n-r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

w,h = map(int,input().split())
mod = 10**9+7
N = h + w + 1
fact = [1,1]
factinv = [1,1]
inv = [0,1]

for i in range(2,N+1):
    fact.append((fact[-1]*i) % mod)
    inv.append((-inv[mod%i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

print(cmb(h+w-2,h-1))