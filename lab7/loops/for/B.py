N = int(input())
s = 1
if(N ==1 or N==0):
    print(1)
else:
    for i in range(1, N+1):
        s = s*i
print(s)