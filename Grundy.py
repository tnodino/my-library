from sys import setrecursionlimit
setrecursionlimit(10**8)

def dfs(now,before):
    if grundy[now] != -1:
        return grundy[now]
    res = 0
    for i in range(len(graph[now])):
        nxt = graph[now][i]
        if nxt == before:
            continue
        res ^= dfs(nxt,now) + 1
    grundy[now] = res
    return grundy[now]

n = int(input())
graph = [[] for i in range(n)]
for i in range(n-1):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)
grundy = [-1] * n
dfs(0,-1)
if grundy[0]:
    print('Alice')
else:
    print('Bob')