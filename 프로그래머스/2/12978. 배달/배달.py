from heapq import heappush, heappop
def solution(N, road, K):
    answer = 0
    MAX = K+1 # 보통은 MAX를 점 개수*간선의 최대 길이보다 크게 주지만
    # 이 경우에는 K보다 큰 값은 의미가 없기 때문에 MAX를 1+K로 준다.
    # 다익스트라에서 MAX가 작을수록 연산이 줄어들기 때문에
    # 이 값은 작게 주는 것이 유리하다.
    
    adj = [{} for _ in range(N+1)]
    for a,b,c in road:
        if a not in adj[b]:
            adj[a][b] = MAX
            adj[b][a] = MAX
        adj[a][b] = adj[b][a] = min(adj[a][b],c)
    
    dist = [MAX]*(N+1)
    dist[1] = 0
    H = [(0,1)]
    while H:
        d, cur = heappop(H)
        for nxt in adj[cur]:
            nd = adj[cur][nxt]
            if nd+d >= dist[nxt]:
                continue
            dist[nxt] = nd+d
            heappush(H,(nd+d,nxt))
        
    for i in dist:
        if i < MAX:
            answer += 1
    return answer