import sys


N,M=map(int,sys.stdin.readline().split())
mat=[[0]*(N+1)]
for i in range(N):
    a=[0]+list(map(int,sys.stdin.readline().split()))
    for j in range(1,N+1):
        a[j]+=a[j-1]
    mat.append(a)
for i in range(1,N+1):
    for j in range(N+1):
        mat[i][j]+=mat[i-1][j]
for i in range(M):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    print(mat[x2][y2]-mat[x1-1][y2]-mat[x2][y1-1]+mat[x1-1][y1-1])
