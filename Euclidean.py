def _inv_gcd(a, b):
    a %= b
    if a == 0:
        return (b, 0)
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0:
        m0 += b // s
    return (s, m0)

def crt(r, m):
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue
        g, im = _inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g:
            return (0, 0)
        x = (r1 - r0) // g % u1 * im % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return (r0, m0)

t = int(input())
INF = 10 ** 36
for _ in range(t):
    x, y, p, q = map(int,input().split())
    ans = INF
    for t1 in range(x, x + y):
        for t2 in range(p, p + q):
            # t = t1 mod x
            # t = t2 mod y
            # crt([t1,t2],[x,y])
            t, lcm = crt([t1, t2], [2 * x + 2 * y, p + q])
            if lcm == 0:
                continue
            if ans > t:
                ans = t
    if ans == INF:
        ans = 'infinity'
    print(ans)
