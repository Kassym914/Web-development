n = list(map(int, input().split()))
s = max(n)
for i in range(len(n)):
    if(n[i] == s):
        k = i
        break
print(s, k)