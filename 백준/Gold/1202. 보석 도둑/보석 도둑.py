import sys
from heapq import heappop, heappush
input = sys.stdin.readline


N, K = map(int,input().split())
J = sorted ( tuple(map(int,input().split())) for _ in range(N))
H = []
B = sorted( int(input()) for _ in range(K))

J.append( (1e10,1e10))

jidx = 0
rst = 0
for i in range(K):
    while J[jidx][0]<=B[i]:
        heappush(H,-J[jidx][1])
        jidx += 1

    if H:
        rst += heappop(H)


print(-rst)
