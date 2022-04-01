def Minfour(a, b , c ,d ):
    x = min(a,b,c,d)
    return(x)
n = list(map(int, input().split()))
print(Minfour(n[0], n[1], n[2], n[3]))