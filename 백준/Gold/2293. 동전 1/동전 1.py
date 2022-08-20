import sys
input=sys.stdin.readline

n, k = map(int,input().split())

DP=[0]*(k+1)
DP[0]=1
L=[int(input()) for i in range(n)]

for i in L: 
    for j in range(i,k+1):
        
        DP[j]+=DP[j-i]
        
        
print(DP[-1])
