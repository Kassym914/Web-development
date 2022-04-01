v = int(input())
t = int(input())
if v>=0:
    s = v*t
    if s>=109:
        print(s%109)
    else:
        print(s)
else: 
    s = v*t
    if s<-109: 
        k = s%(-109)
        print(109 - k)
    else:
        print(109 + s)