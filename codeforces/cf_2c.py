
import math

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dis(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def check(p, c):
    ret = 0
    for i in range(1, 4):
        ret += ((dis(p, c[i][:2]) / c[i][2] - dis(p, c[(i+1)%3+1][:2]) / c[(i+1)%3+1][2]) ** 2)
    return ret

c = [None] * 4
p0 = [0, 0]

for i in range(1, 4):
    x, y, r = map(float, input().split())
    c[i] = (x, y, r)
    p0[0] += x / 3
    p0[1] += y / 3

s = 1

while s > 1e-6: #something called an EPS, really small number.
    flag = True
    for i in range(4):
        p = [p0[0] + dx[i] * s, p0[1] + dy[i] * s]
        if check(p, c) < check(p0, c):
            p0[0] += dx[i] * s
            p0[1] += dy[i] * s
            flag = False
    if flag:
        s /= 2

if check(p0, c) < 1e-6:
    print("{:.5f} {:.5f}".format(p0[0], p0[1]))
