def segfunc(x, y):
    return x ^ y

ide_ele = 0

class SegTree:
    def __init__(self,segfunc,init_val,ide_ele):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 2 ** n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num-1] = init_val[i]
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2])

    def update(self,k,x):
        k += self.num - 1
        self.seg[k] = self.segfunc(self.seg[k],x)
        while k:
            k = (k-1) // 2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])

    def query(self,l,r):
        if r <= l:
            return self.ide_ele
        l += self.num - 1
        r += self.num - 2
        res = self.ide_ele
        while r - l > 1:
            if l & 1 == 0:
                res = self.segfunc(res,self.seg[l])
            if r & 1 == 1:
                res = self.segfunc(res,self.seg[r])
                r -= 1
            l = l // 2
            r = (r-1) // 2
        if l == r:
            res = self.segfunc(res,self.seg[l])
        else:
            res = self.segfunc(res,self.segfunc(self.seg[l],self.seg[r]))
        return res

n,q = map(int,input().split())
a = list(map(int,input().split()))
seg = SegTree(segfunc,a,ide_ele)
for i in range(q):
    t,x,y = map(int, input().split())
    if t == 1:
        x -= 1
        seg.update(x,y)
    else:
        x -= 1
        print(seg.query(x,y))
