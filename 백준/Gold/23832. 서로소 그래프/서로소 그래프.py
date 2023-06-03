N = int(input())
L = [0]*(N+1)
prime = []

for i in range(2,N+1):
    if L[i] == 0:
        L[i] = i
        prime.append(i)
    for p in prime:
        n = i*p
        if i*p>N:
            break
        L[n] = p
        if i%p == 0:
            break
rst = 0
for i in range(2,N+1):
    ii = i

    while i>1:
        cnt = L[i]
        ii = ii*(L[i]-1)//L[i]
        while i%cnt == 0 and i>1:
            i//=cnt
    rst += ii

print(rst)
    
