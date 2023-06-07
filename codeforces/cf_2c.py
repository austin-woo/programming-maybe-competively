# import math

# p = [[0]*2 for i in range(3)]
# r = [0]*3

# a = [0]*2
# b = [0]*2
# k = [0]*2
# c = [0]*2

# # read input
# for i in range(3):
#     p[i][0], p[i][1], r[i] = map(int, input().split())

# # calculate coefficients
# a[0] = 2*(p[0][0]-p[1][0])
# a[1] = 2*(p[1][0]-p[2][0])
# b[0] = 2*(p[0][1]-p[1][1])
# b[1] = 2*(p[1][1]-p[2][1])
# k[0] = r[1]*r[1] - r[0]*r[0]
# k[1] = r[2]*r[2] - r[1]*r[1]
# c[0] = p[1][0]*p[1][0] - p[0][0]*p[0][0] + p[1][1]*p[1][1] - p[0][1]*p[0][1]
# c[1] = p[2][0]*p[2][0] - p[1][0]*p[1][0] + p[2][1]*p[2][1] - p[1][1]*p[1][1]
# c[0] = -c[0]
# c[1] = -c[1]

# # check if intersection point exists
# if a[1]*b[0]-a[0]*b[1] == 0:
#     exit()

# xr = (k[1]*b[0]-k[0]*b[1])/(a[1]*b[0]-a[0]*b[1])
# xc = (c[1]*b[0]-c[0]*b[1])/(a[1]*b[0]-a[0]*b[1])
# yr = (k[1]*a[0]-k[0]*a[1])/(a[0]*b[1]-a[1]*b[0])
# yc = (c[1]*a[0]-c[0]*a[1])/(a[0]*b[1]-a[1]*b[0])

# af = xr*xr+yr*yr
# bf = 2*xc*xr-2*p[1][0]*xr+2*yc*yr-2*p[1][1]*yr-r[1]*r[1]
# cf = xc*xc-2*p[1][0]*xc+p[1][0]*p[1][0]+yc*yc-2*p[1][1]*yc+p[1][1]*p[1][1]
# deta = bf*bf-4*af*cf

# if af==0:
#     if bf==0 and cf!=0:
#         exit()
#     if bf*cf>0:
#         exit()
#     x = xc
#     y = yc
# elif deta<0:
#     exit()
# else:
#     deta = math.sqrt(deta)
#     maxd = deta-bf
#     mind = -bf-deta
#     if mind<0:
#         mind = maxd
#     if maxd<0:
#         exit()
#     else:
#         rs = mind/2/af
#         x = xr*rs+xc
#         rs = mind/2/af
# x = xr*rs+xc
# y = yr*rs+yc
# print("{:.5f} {:.5f}".format(x, y))

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
