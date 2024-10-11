a, b = map(int, input().split())

def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n
d = gcd(a, b)

k = [10] * (max(a,b)+1)
for i in range(1, max(a,b)+1):
    x = (d-b*i)/a
    if x == int(x):
        k[i] = i
y = min(k)
x = int((d-b*y)/a)
print(x, y, d)
