class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev_graph = [[] for _ in range(n)]
        self.labels = [-1] * n
        self.lb_cnt = 0

    def add_edge(self, v, nxt_v):
        self.graph[v].append(nxt_v)
        self.rev_graph[nxt_v].append(v)

    def build(self):
        self.post_order = []
        self.used = [False] * self.n
        for v in range(self.n):
            if not self.used[v]:
                self._dfs(v)
        for v in reversed(self.post_order):
            if self.labels[v] == -1:
                self._rev_dfs(v)
                self.lb_cnt += 1

    def _dfs(self, v):
        stack = [v, 0]
        while stack:
            v, idx = stack[-2:]
            if not idx and self.used[v]:
                stack.pop()
                stack.pop()
            else:
                self.used[v] = True
                if idx < len(self.graph[v]):
                    stack[-1] += 1
                    stack.append(self.graph[v][idx])
                    stack.append(0)
                else:
                    stack.pop()
                    self.post_order.append(stack.pop())

    def _rev_dfs(self, v):
        stack = [v]
        self.labels[v] = self.lb_cnt
        while stack:
            v = stack.pop()
            for nxt_v in self.rev_graph[v]:
                if self.labels[nxt_v] != -1:
                    continue
                stack.append(nxt_v)
                self.labels[nxt_v] = self.lb_cnt

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.scc = SCC(2 * n)

    def add_clause(self, i, f, j, g):
        self.scc.add_edge(2 * i + int(not f), 2 * j + int(g))
        self.scc.add_edge(2 * j + int(not g), 2 * i + int(f))

    def satisfy(self):
        self.scc.build()
        self.ans = [False] * self.n
        for i in range(self.n):
            if self.scc.labels[2 * i] == self.scc.labels[2 * i + 1]:
                return False
            self.ans[i] = self.scc.labels[2 * i] < self.scc.labels[2 * i + 1]
        return True

    def answer(self):
        return self.ans


n, d = map(int, input().split())
info = [list(map(int,input().split())) for i in range(n)]
ts = TwoSAT(n)
for i in range(n):
    xi, yi = info[i]
    for j in range(i+1, n):
        xj, yj = info[j]
        if abs(xi - xj) < d:
            ts.add_clause(i, False, j, False)
        if abs(xi - yj) < d:
            ts.add_clause(i, False, j, True)
        if abs(yi - xj) < d:
            ts.add_clause(i, True, j, False)
        if abs(yi - yj) < d:
            ts.add_clause(i, True, j, True)
if not ts.satisfy():
    print("No")
else:
    print("Yes")
    for i, flag in enumerate(ts.answer()):
        if flag:
            print(info[i][0])
        else:
            print(info[i][1])