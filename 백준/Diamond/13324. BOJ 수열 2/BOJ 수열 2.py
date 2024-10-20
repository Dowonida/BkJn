from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N = int(input())

L = list(map(int,input().split()))

for i in range(N):
    L[i] -= i

H = []
stk = []

for i in L:
    heappush(H,-i)
    if -H[0] > i:
        heappop(H)
        heappush(H,-i)
    stk.append(-H[0])

for i in range(N-2,-1,-1):
    stk[i] = min(stk[i],stk[i+1])

ans = 0    
for i in range(N):
    ans += abs(stk[i]-L[i])
    stk[i] += i
    
for i in stk:
    print(i)
