import sys
input = sys.stdin.readline

N = int(input())

adj = [ [] for _ in range(N+1)]

for i in range(N-1):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))


depth = [0]*(N+1)
parent = [0]*(N+1) #부모 노드
dist = [0]*(N+1) #부모로 가는 거리

stk = [1]
depth[1] = 1
while stk:
    a = stk.pop()
    dd = depth[a]
    for p, d in adj[a]:
        if depth[p]:
            continue
        depth[p] = dd+1
        parent[p] = a
        dist[p] = d
        stk.append(p)

dist = [dist]
parent = [parent]

flag = 1
while flag:
    flag = 0
    pcnt = [0]
    dcnt = [0]

    for i in range(1,N+1):
        myp = parent[-1][i]
        pcnt.append( parent[-1][myp])
        dcnt.append( dist[-1][i]+dist[-1][myp])
        flag = max(flag,parent[-1][myp])

    if flag:
        parent.append(pcnt)
        dist.append(dcnt)
        
D = len(dist)
for _ in range(int(input())):
    rst = 0
    a,b = map(int,input().split())
    if depth[a]>depth[b]:
        a,b = b,a
    diff  = depth[b]-depth[a]
    #왼쪽이 더 깊이가 낮음, 오른쪽이 올라가야함
    for i in range(D):
        if (1<<i)&diff:
            
            rst += dist[i][b]
            b = parent[i][b]
            
    while parent[0][a]!=parent[0][b]:
        for i in range(D):
            if parent[i][a] != parent[i][b]:
                rst += dist[i][a] + dist[i][b]
                a = parent[i][a]
                b = parent[i][b]
                
    if a!= b:

        rst += dist[0][a] + dist[0][b]

    print(rst)