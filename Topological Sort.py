from collections import defaultdict, deque
n,m = map(int,input().split())
es = []
for i in range(n-1+m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    es.append(tuple((a,b)))

in_cnt = defaultdict(int)
outs = defaultdict(list)
rev = defaultdict(list)
for v1,v2 in es:
    in_cnt[v2] += 1
    outs[v1].append(v2)
    rev[v2].append(v1)

res = []
queue = deque([v1 for v1 in range(n) if in_cnt[v1] == 0])
while queue:
    v1 = queue.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            queue.append(v2)

order = [i for i,v in sorted(enumerate(res), key=lambda x: x[1])]

ans = [0 for i in range(n)]
for v1 in res[:0:-1]:
    ans[v1] = max([(order[v2], v2) for v2 in rev[v1]])[1] + 1
print(*ans, sep='\n')