import sys
from heapq import heappop, heappush

input =  sys.stdin.readline

N, M = map(int,input().split())
adj = [ {} for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    if b in adj[a]:
        d = min(adj[a][b],c)
        adj[a][b] = d
    else:
        adj[a][b] = c

Max = 10000000 # 10000*1000
dist = [Max]*(N+1)
dist[1] = 0
#벨만포드 N-1번 돌고 N번 부터는 무한 루프인 이유
#N-1번째에 갱신된 점은 최단거리의 간선 수가 N-1개란 뜻이다.
#마찬가지로 N번째에 갱신된 점은 최단거리가 N개의 간선을 지났고
#이 말은 노드를 N+1개 지났다는 뜻이다.
#전체 노드는 N개이므로 특정 노드를 두번 지났단 뜻이고
#따라서 특정 노드를 두번째로 지날 땐 그 전보다 비용이 줄었단 뜻이다.
visited = [0]*(N+1)
visited[1] = 1
for i in range(N-1):

    for point in range(1,N+1):
        if visited[point] == 0:
            continue
        for j in adj[point]:
            visited[j] = 1
            dist[j] = min(dist[j],dist[point]+adj[point][j])
            
            
for point in range(1,N+1):
    if visited[point] ==0:
        continue
    for j in adj[point]:
        if dist[j] > dist[point]+adj[point][j]:
            print(-1)
            break
    else:
        continue
    break
else:
    for i in range(2,N+1):
        if dist[i]==Max:
            print(-1)
        else:
            print(dist[i])
    
