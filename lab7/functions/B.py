def double_power(a, b ):
    return(pow(a, b))
n = list(map(int, input().split()))
print(double_power(n[0], n[1]))