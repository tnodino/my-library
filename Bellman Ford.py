def bellman_ford(r):
    dist = [float('inf') for i in range(v)]
    dist[r] = 0
    for i in range(v):
        update = False
        for x,y,z in graph:
            if dist[x] + z < dist[y]:
                dist[y] = dist[x] + z
                update = True
        if not update:
            break
        if i == v - 1:
            return -1
    return dist

v,e,r = map(int,input().split())
INF = 10**18
graph = []
for i in range(e):
    s,t,d = map(int,input().split())
    graph.append([s,t,d])
dist = bellman_ford(r)
if dist == -1:
    print('NEGATIVE CYCLE')
    exit(0)
for d in dist:
    if d == float('inf'):
        print('INF')
    else:
        print(d)