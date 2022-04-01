n = int(input())
i = 1
s =1 
while i < n:
    s = s*2
    if(s>n):
        print(i)
        break
    i = i+1