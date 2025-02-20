a = input()
m = 'AHIMOTUVWXY18'
n = 'EJSZ'
p = '3L25'
b = ''
for i in range(len(a)):
    if a[i] in m:
        b += a[i]
    elif a[i] in n:
        q = n.index(a[i])
        b += p[q]
    elif a[i] in p:
        q = p.index(a[i])
        b += n[q]
if len(a) == len(b):
    if a == b and a == a[::-1]:
        print(a, "is a mirrored palindrome.")
    elif a == b[::-1]:
        print(a, "is a mirrored string.")
else:
    if a == a[::-1]:
        print(a, "is a regular palindrome.")
    else:
        print(a, "is not a palindrome.")