class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

n = int(input())
a = list(map(int,input().split()))
bit = BinaryIndexedTree(n+1)

ans = 0
for x in reversed(a):
    ans += bit.sum(x)
    bit.add(x,1)
print(ans)