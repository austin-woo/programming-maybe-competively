# import math
# n, m, a = map(int, input().split())

# print(math.ceil(n/a) + math.ceil(m/a))  

n,m,a = map(int, input().split)
if m%a ==0:
    v = m //a
else:
    v = m // a + 1

if n%a ==0:
    v2 = n //a
else:
    v2 = n //a + 1

print(v * v2)