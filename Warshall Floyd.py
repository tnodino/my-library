n,m = map(int,input().split())
INF = float('inf')
cost = [[INF] * n for i in range(n)]
for i in range(n):
    cost[i][i] = 0
for i in range(m):
    a,b,t = map(int,input().split())
    cost[a][b] = t
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
for i in range(n):
    if cost[i][i] < 0:
        print('NEGATIVE CYCLE')
        exit(0)
for x in cost:
    x = [str(i).replace('inf','INF') for i in x]
    print(' '.join(x))