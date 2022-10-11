import sys
input=sys.stdin.readline

N,T=map(int,input().split())

DP=[0]*(T+1)
L=[ list(map(int,input().split())) for i in range(N)]

for time, score in L:
    for i in range(T,time-1,-1):
        DP[i]=max(DP[i],DP[i-time]+score)
print(DP[-1])
