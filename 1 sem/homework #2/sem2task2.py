n, l = map(str, input().split())
n = int(n)
m = ''
for i in range(0, len(l), n):
    k = l[i:i+n]
    m = m + k[::-1]
print(m)