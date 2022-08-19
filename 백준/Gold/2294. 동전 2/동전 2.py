import sys
input=sys.stdin.readline

n, k = map(int,input().split())
DP=[0]+[-1]*(k)

L=[]
for i in range(n):
    L.append(int(input()))


for i in range(min(L),k+1):
    Min=1000000
    for j in L:
        if j<=i and DP[i-j]!=-1:
            Min=min(DP[i-j],Min)
        DP[i]= Min+1 if Min<=100000 else -1
print(DP[-1])
            

