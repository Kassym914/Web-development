n = list(map(int, input().split()))
for i in range(len(n)):
    if(n[i]>0 and n[i+1]>0) or (n[i]<0 and n[i+1]<0):
        print(n[i], n[i+1])
        break