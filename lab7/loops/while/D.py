n = int(input())
i = 1
s=2 
if(n ==s or n == 1):
    print("YES")
else: 

    while i<n:
        if(s>n):
            print("NO")
            break
        s = s*2 
        if(s==n):
            print("YES")
            break
    