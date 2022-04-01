n = list(map(int, input().split()))
cnt = 0
for i in range(len(n)):
    if(n[i]>0):
        cnt+=1
print(cnt)