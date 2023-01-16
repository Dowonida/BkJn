import bisect
import sys
input = sys.stdin.readline

N = int(input()) +1

L = [0]+list(map(int,input().split()))

update = [(0,0)]
read = [[]]

RST = []

idx = 0
for _ in range(int(input())):
    A = map(int,input().split())
    if next(A) == 1:
        i, v = A
        update.append( (i,v))
        read.append( [])
    else:
        k,i,j = A
        read[k].append( (idx,i,j))
        RST.append(0)
        idx += 1

seg = [0]*N+L
for i in range(N-1,0,-1):
    seg[i] = seg[i*2]+seg[i*2+1]

for i in range(len(update)):
    n, v = update[i]
    idx = n+N
    diff = v - seg[idx]
    while idx:
        seg[idx] += diff
        idx //= 2

    for a,b,c in read[i]:
        #RST[a]에 더함
        s = b+N
        e = c+N+1
        while s<e:
            if s%2:
                RST[a] += seg[s]
                s += 1
            if e%2:
                e -= 1
                RST[a] += seg[e]
            s//=2
            e//=2
print(*RST)
