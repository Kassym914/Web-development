import math
a = int(input())
n = int(input())
s = 1
for i in range(1, n+1):
    s = s + pow(a, i)
print(s)