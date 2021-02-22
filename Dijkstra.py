from heapq import heappop,heappush
v,e,r = map(int,input().split())
INF = 10**18
graph = [[] for i in range(v)]
for i in range(e):
    s,t,d = map(int,input().split())
    graph[s].append([t,d])
dist = [INF for i in range(v)]
dist[r] = 0
pq = [(0,r)]
while pq:
    d,node = heappop(pq)
    if d > dist[node]:
        continue
    for next,cost in graph[node]:
        if d + cost < dist[next]:
            dist[next] = d + cost
            heappush(pq,(dist[next],next))
for d in dist:
    if d == INF:
        print('INF')
    else:
        print(d)