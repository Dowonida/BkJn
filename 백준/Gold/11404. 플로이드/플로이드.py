import sys
input=sys.stdin.readline


n=int(input())
m=int(input())

M=[ [10000000 for i in range(n)] for j in range(n)]
for i in range(n):
    M[i][i]=0
for i in range(m):
    s, e, c = map(int,input().split())
    s-=1
    e-=1
    M[s][e]=min(M[s][e],c)



for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j]=min(M[i][j],M[i][k]+M[k][j])



for i in range(n):
    for j in range(n):
        if M[i][j]==10000000:
            M[i][j]=0

for i in M:
    print(*i)
