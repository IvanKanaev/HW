n, m = [int(i) for i in input().split()]
t = []
for i in range(n):
    temp = [0 for j in range(m)]
    t.append(temp)
x,y,= 0, 0
k = int(1)
t[0][0]=1
while k < m*n:
    if x + 1 < m:
        if t[y][x+1] == 0:
            x+=1
            k+=1
            t[y][x] = k
            continue
    if y+1< n:
        if t[y+1][x] == 0:
            y+=1
            k+=1
            t[y][x] = k
            continue
    if t[y][x-1] == 0 and x-1>=0:
        x-=1
        k+=1
        t[y][x] = k
        continue
    while t[y-1][x] == 0:
        y-=1
        k+=1
        t[y][x] = k

for row in t:
    print(*row)
