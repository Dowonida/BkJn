import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
Q = [ [] for _ in range(N+1)]
for i in range(N):
    a,b = map(int,input().split())
    Q[a].append(-b)
H = []
rst = 0
for i in range(N,0,-1):
    for j in Q[i]:
        heappush(H,j)
    if not H:
        continue
    rst += heappop(H)
print(-rst)
