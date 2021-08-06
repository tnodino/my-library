def color(x):
    if x == 'R':
        return 0
    if x == 'G':
        return 1
    if x == 'B':
        return 2

n = int(input())
s = list(input())
r = list(input())
for i in range(n):
    s[i] = color(s[i])
    r[i] = color(r[i])

ans = 0
mod = 10**9+7
for i in range(3):
    t = []
    for j in range(n):
        t.append((i - r[j] + 3) % 3)
    p = 1
    hash1 = 0
    hash2 = 0
    for j in range(n):
        hash1 = hash1 * 3 + s[j]
        hash1 %= mod
        hash2 = hash2 + p * t[n-j-1]
        hash2 %= mod
        if hash1 == hash2:
            ans += 1
        p *= 3
        p %= mod
    p = 1
    hash1 = 0
    hash2 = 0
    for j in range(n-1):
        hash1 = hash1 + p * s[n-j-1]
        hash1 %= mod
        hash2 = hash2 * 3 + t[j]
        hash2 %= mod
        if hash1 == hash2:
            ans += 1
        p *= 3
        p %= mod
print(ans)