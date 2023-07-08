from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

adj = [ {} for _ in range(N+1)]
Max = 100000000000

dist = [ [Max]*(K+1) for _ in range(N+1)]
#dist[i][j]는 i점을 단축k개 남기고 간 최단거리


#dist[1] = [0]*(K+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    if a not in adj[b]:
        adj[b][a] = Max
    if b not in adj[a]:
        adj[a][b] = Max
    adj[a][b] = min(adj[a][b],c)
    adj[b][a] = min(adj[b][a],c)


#push할 때 점,남은포장,거리
#제일 처음에는 (1.K,0)
H = [(0,1,K)] #점,포장, 거리
while H:
    cur_d,cur_p,cur_k = heappop(H)
    if cur_d>dist[cur_p][cur_k]:
        continue
    for nxt_p in adj[cur_p]:
        nxt_d = cur_d+adj[cur_p][nxt_p]
        if nxt_d < dist[nxt_p][cur_k]:
            dist[nxt_p][cur_k] = nxt_d
            heappush(H,(nxt_d,nxt_p,cur_k))
        if cur_k and (cur_d<dist[nxt_p][cur_k-1]):
            dist[nxt_p][cur_k-1] = cur_d
            heappush(H,(cur_d,nxt_p,cur_k-1))
    

print(min(dist[N]))
