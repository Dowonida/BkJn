import sys
input = sys.stdin.readline

N, M = map(int,input().split())
L = [ list(map(int,input().split())) for _ in range(N)]

LL = [ [0]*(N+1) for _ in range(N+1)]

for _ in range(M-1):
    a,b,c,d,e,f = map(int,input().split())
    LL[b][c] += f
    LL[b][e+1] -= f
    LL[d+1][c] -= f
    LL[d+1][e+1] += f

for r in range(N+1):
    for c in range(1,N+1):
        LL[r][c] += LL[r][c-1]

for c in range(N+1):
    for r in range(1,N+1):
        LL[r][c] += LL[r-1][c]

a,b,c,d,e = map(int,input().split())


rst = 0
for R in range(b,d+1):
    for C in range(c,e+1):
        rst += L[R][C] + LL[R][C]
print(rst)
