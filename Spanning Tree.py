from heapq import heappop,heappush
v,e = map(int,input().split())
graph = [[] for i in range(v)]
for i in range(e):
    s,t,w = map(int, input().split())
    graph[s].append((t,w))
    graph[t].append((s,w))
visit = [0] * v
pq = []
for t,w in graph[0]:
    heappush(pq,(w,t))
visit[0] = 1
ans = 0
while pq:
    w,t = heappop(pq)
    if visit[t]:
        continue
    visit[t] = 1
    ans += w
    for s,w in graph[t]:
        if visit[s] == 0:
            heappush(pq,(w,s))
print(ans)