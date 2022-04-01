def xor(x, y):
    if(x==1 and y == 1) or (x == 0 and y == 0):
        return(0)
    else:
        return(1)
n = list(map(int, input().split()))
print(xor(n[0], n[1]))