from heapq import heappop, heappush

def solution(n, start, end, roads, traps):
    # on off를 위해서 인접 행렬이 좋을 듯
    # trap = set(traps) -> trap의 길이가 10이니까 그냥 쓰자. 인덱스가 필요하다
    trap_idx = {traps[i] : i for i in range(len(traps))}
    adj = [[0]*(n+1) for _ in range(n+1)] #a to b = adj[a][b] if not traped else adj[b][a]
    # 주의점: 2 -> 3으로 가는 길만 있는데, 둘 다 함정인 경우
    # 판별법: 그냥 두 번 뒤집어주면 된다.
    # 같은 점을 방문했더라도 트랩의 상태에 따라 다르다.
    # visited는 들어갈 때의 기준으로 저장
    for a,b,c in roads:
        if adj[a][b] == 0:
            adj[a][b] = c
        adj[a][b] = min(adj[a][b],c)
    
    MAX = 1000000000
    visited = [ [MAX]*(1024) for _ in range(n+1) ]
    visited[start][0] = 0
    H = [(0,start,0)] #거리 0, 현재 위치, 트랩여부
    while H:
        
        cur_d, cur_p, cur_t = heappop(H)
        if cur_d >= MAX:
            continue
        if visited[cur_p][cur_t] < cur_d: #같은 점에 같은 상황으로 더 짧게 온 적이 있는 경우 무시
            continue
        if cur_p in trap_idx:
            cur_t ^= 1<<(trap_idx[cur_p])

        for i in range(1,n+1):
            s, e = cur_p, i
            if (cur_p in trap_idx) and (cur_t &(1<<trap_idx[cur_p])):
                s,e = e,s
            if (i in trap_idx) and (cur_t & (1<<trap_idx[i])):
                s,e = e,s
            if not adj[s][e]:
                continue
            n_d = cur_d + adj[s][e]
            if n_d < visited[i][cur_t]:
                if i == end:
                    MAX = min(MAX, n_d)
                    continue
                visited[i][cur_t] = n_d
                heappush(H,(n_d, i, cur_t))
        
        
    
    
    #answer = min(visited[end])
    #assert MAX>answer
    return MAX