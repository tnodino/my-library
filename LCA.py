from collections import deque
n = int(input())
edge = [[] for _ in range(n)]
for i in range(n-1):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    edge[x].append(y)
    edge[y].append(x)

depth = [-1] * n
depth[0] = 0
queue = deque()
queue.append(0)
while queue:
    x = queue.popleft()
    for y in edge[x]:
        if depth[y] != -1:
            continue
        depth[y] = depth[x] + 1
        queue.append(y)

before = [0] * n
for x in range(1,n):
    for y in edge[x]:
        if depth[y] < depth[x]:
            before[x] = y
            break

def doubling(a,n):
    m = len(a)
    result = {}
    result[1] = a
    x = 2
    while x <= n:
        a = [a[a[i]] for i in range(m)]
        result[x] = a
        x *= 2
    return result

ancestor = doubling(before,max(depth))

def get_ancestor(a,n):
    x = 1
    while n:
        if n & x:
            a = ancestor[x][a]
            n -= x
        x *= 2
    return a

def lca(a,b):
    if depth[b] > depth[a]:
        a,b = b,a
    a = get_ancestor(a,depth[a]-depth[b])
    if a == b:
        return a
    ng = 0
    ok = depth[a]
    while ng < ok - 1:
        m = ng + (ok - ng) // 2
        if get_ancestor(a,m) == get_ancestor(b,m):
            ok = m
        else:
            ng = m
    return get_ancestor(a,ok)

q = int(input())
for i in range(q):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    c = lca(a,b)
    print(depth[a] + depth[b] - 2 * depth[c] + 1)