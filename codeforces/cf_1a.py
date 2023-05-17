
# n, m, a = map(int, input().split())

n = 6
m = 6
a = 4
#answer should be 4

if n%a == 0: 
    num1 = n//a 
else : 
    num1 = (n//a)+1 
if m%a == 0: 
    num2 = m//a 
else : 
    num2 = (m//a)+1

print(int(num1*num2))

# n,m,a = map(int, input().split)
# if m%a ==0:
#     v = m //a
# else:
#     v = m // a + 1

# if n%a ==0:
#     v2 = n //a
# else:
#     v2 = n //a + 1

# print(v * v2)
# print(math.ceil(n/a) + math.ceil(m/a))  