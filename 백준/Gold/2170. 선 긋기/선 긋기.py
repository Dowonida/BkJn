import sys
input=sys.stdin.readline
N=int(input())
L=[]
for i in range(N):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    L.append([a,b])

L.sort()
RST=[L[0]]
for i in range(1,N):
    if L[i][0]<=RST[-1][1]:
        RST[-1][1]=max(RST[-1][1],L[i][1])
    else:
        RST.append(L[i])
rst=0
for i in RST:
    rst+=i[1]-i[0]
print(rst)
