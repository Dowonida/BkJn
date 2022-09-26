import sys
input=sys.stdin.readline
M=1000000
DP=[1]*(M+1)
SUM=[0]*(M+1)
for i in range(2,(M+1)):
    j=1
    while i*j<=M:
        DP[i*j]+=i
        j+=1

for i in range(1,M+1):
    SUM[i]=SUM[i-1]+DP[i]
t=int(input())
for _ in range(t):
    print(SUM[int(input())])