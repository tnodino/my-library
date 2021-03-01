class UnionFind:
    def __init__(self, n):
        self.root = [-1] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.root[x] > self.root[y]:
                x,y = y,x
            self.root[x] += self.root[y]
            self.root[y] = x
        return x

n,q = map(int,input().split())
uf = UnionFind(n)
for i in range(q):
    t,u,v = map(int,input().split())
    if t == 0:
        uf.union(u,v)
    if t == 1:
        if uf.find(u) == uf.find(v):
            print(1)
        else:
            print(0)