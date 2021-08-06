from math import sqrt
class SolvCircle:
    def __init__(self):
        self.loop_max = 100
        self.convrgv = 1.0e-9

    def solv_circle(self, pt_x, pt_y):
        mv_rate  = 0.5
        max_dist = 0.0
        xsv = 0.0
        ysv = 0.0
        cx = 0.0
        cy = 0.0
        k = 0
        cvgflg = False
        while cvgflg == False:
            for t in range(self.loop_max):
                max_dist = 0.0
                for i in range(len(pt_x)):
                    dist = self.distance(cx, cy, pt_x[i], pt_y[i])
                    if dist > max_dist:
                        max_dist = dist
                        k = i
                cx += (pt_x[k] - xsv) * mv_rate
                cy += (pt_y[k] - ysv) * mv_rate
                if self.distance(cx, cy, xsv, ysv) <= self.convrgv:
                    cx = xsv
                    cy = ysv
                    cvgflg = True
                    break
                xsv = cx
                ysv = cy
            mv_rate /= 2.0
        return [cx, cy, max_dist]

    def distance(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        return sqrt(dx * dx + dy * dy)

n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
x,y = [list(i) for i in zip(*l)]
sc = SolvCircle()
print(sc.solv_circle(x,y)[2])