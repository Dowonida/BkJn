import sys
input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

parent= [0]*(N+1)
stk = [1]
depth = [0]*(N+1)
depth[1] = 1
while stk:
    cur = stk.pop()
    for i in adj[cur]:
        if depth[i]:
            continue
        parent[i] = cur
        depth[i] = depth[cur]+1
        stk.append(i)
parent[1] = 0

parent = [parent]

while True:
    cnt = [0]*(N+1)
    for i in range(2,N+1):
        cnt[i] = parent[-1][parent[-1][i]]

    if max(cnt):
        parent.append(cnt)
    else:
        break

def lca(a,b):
    if depth[a]>depth[b]:
        a,b = b,a #b가 더 깊다

    diff = depth[b]-depth[a]
    for i in range(len(parent)):
        if diff&(1<<i):
            b = parent[i][b]

    for i in range(len(parent)-1,-1,-1):
        if parent[i][a] != parent[i][b]:
            a,b = parent[i][a], parent[i][b]
    if a!=b:
        return parent[0][a]
    
    return a
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    print(sorted((lca(a,b),lca(a,c),lca(b,c)), key = lambda x: depth[x])[-1])
