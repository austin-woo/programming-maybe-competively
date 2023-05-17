import math

PI = math.pi
point = [[0 for j in range(2)] for i in range(3)]
ql = [0 for i in range(3)]
cosa = [0 for i in range(3)]
qsina = [0 for i in range(3)]
qsina_0 = 0
qsina_1 = 0
qsina_2 = 0
a = [0 for i in range(3)]
b = [1 for i in range(3)]
c = [0 for i in range(3)]
d = 0
mind = -1
res = 0
qr = 0
s = 0

for i in range(3):
    point[i][0], point[i][1] = map(float, input().split())

for i in range(3):
    ql[i] = (point[i][0] - point[(i + 1) % 3][0]) ** 2 + (point[i][1] - point[(i + 1) % 3][1]) ** 2

for i in range(3):
    cosa[i] = (ql[(i + 2) % 3] + ql[(i + 1) % 3] - ql[i]) / (2 * math.sqrt(ql[(i + 1) % 3]) * math.sqrt(ql[(i + 2) % 3]))
    qsina[i] = 1 - cosa[i] * cosa[i]
    if i == 0:
        qsina_0 = qsina[i]
    elif i == 1:
        qsina_1 = qsina[i]
    else:
        qsina_2 = qsina[i]
    a[i] = int(math.acos(cosa[i]) * 1e5)

qr = (ql[0] / qsina[0] + ql[1] / qsina[1] + ql[2] / qsina[2]) / 12

while sum(b) <= 100:
    c[0] = a[0] // b[0]
    c[1] = a[1] // b[1]
    c[2] = a[2] // b[2]
    d = abs(c[0] - c[1]) + abs(c[1] - c[2]) + abs(c[2] - c[0])
    if mind == -1 or mind > d:
        mind = d
        res = b[0] + b[1] + b[2]
    i = 0
    if a[0] // b[0] < a[1] // b[1]:
        i = 1
    if a[i] // b[i] < a[2] // b[2]:
        i = 2
    b[i] += 1

s = qr * math.sin(2 * PI / res) * res / 2
print("%.8f" % s)
