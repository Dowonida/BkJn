import sys
input = sys.stdin.readline

N, M = map(int,input().split())

rst = [0]*(N+1)

adj = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)


for i in range(1,N+1):
    stk = [i]
    visited = [0]*(N+1)
    visited[i] = 1
    while stk:
        cur = stk.pop()
        rst[cur] += 1
        for nxt in adj[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            stk.append(nxt)
    
Max = 0
RST = []
for i, num in enumerate(rst):
    if num == Max:
        RST.append(i)
    elif num>Max:
        Max = num
        RST = [i]
print(*RST)
