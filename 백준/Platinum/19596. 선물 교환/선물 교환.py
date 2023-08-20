import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int,input().split())
    rst = [None]*M
    edges = []
    adj = [ [] for _ in range(N+1)]
    for idx in range(M):
        a,b = map(int,input().split())
        edges.append((a,b))
        adj[a].append(idx)
        adj[b].append(idx)
    for start in range(1,N+1):
        parity = 1
        while adj[start]:
            parity = 1-parity
            cur = start 
            while adj[cur]:
                edge_idx = adj[cur].pop()
                if rst[edge_idx] != None:
                    continue
                edge = edges[edge_idx]
                if edge[parity] == cur:
                    rst[edge_idx] = '0'
                    cur = edge[1-parity]
                else:
                    rst[edge_idx] = '1'
                    cur = edge[parity]
    print(''.join(rst))