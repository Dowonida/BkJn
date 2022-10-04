import sys
input=sys.stdin.readline
dic={}#가격별 최대 인원

C, N =map(int,input().split())
#cost=[ list(map(int,input().split())) for i in range(N)]
cost={}
for i in range(N):
    a,b=map(int,input().split())
    if a not in cost:
        cost[a]=b
    else:
        cost[a]=max(cost[a],b)
DP=[ 0 for i in range(C+1)]#사람 수임

for i in range(1,C+1):
    b=1e10
    for j in cost:
        idx=max(0, i-cost[j])
        b=min(b,DP[idx]+j)
    DP[i]=b
print(DP[-1])
