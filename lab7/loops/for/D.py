n = int(input())
k = int(input())
sn = 1
for i in range(1, n+1):
    sn = sn * i
sk = 1
for i in range(1, k+1):
    sk = sk*i
skn = 1
for i in range(1, n - k +1 ):
    skn = skn*i
c = int(sn/(sk*skn))
print(c)