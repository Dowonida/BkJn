import sys
from heapq import heappop, heappush
input = sys.stdin.readline


N = int(input())
M = int(input())

Max = 100000**2
adj = [{} for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    if b not in adj[a]:
        adj[a][b] = Max
    adj[a][b] = min(adj[a][b],c)


visited = [0]*(N+1)
dist = [Max]*(N+1)


s,e = map(int,input().split())
#dist[s] = 0
H = [ (0,s)]
while H:
    D,P = heappop(H)
    if dist[P]<D:
        continue
    for nxt,nd in adj[P].items():
        if dist[nxt]>nd+D:
            heappush(H,(nd+D,nxt))
            dist[nxt] = nd+D
print(dist[e])
