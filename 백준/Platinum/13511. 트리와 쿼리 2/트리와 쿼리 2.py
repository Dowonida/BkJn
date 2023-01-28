import sys
input = sys.stdin.readline

N = int(input())

adj = [ [] for _ in range(N+1)] #(인접,비용)형태로 저장

for i in range(N-1):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

parent = [0]*(N+1) #부모가 누군지
dist = [0]*(N+1) #부모까지의 거리

#비용은 여느 공통조상과 똑같이 구하면 될거고
#k번째 수는 이진법이용해서 올라갔다 내려가면 됨

stk = [1]
depth = [0]*(N+1)
depth[1] = 1

while stk:
    a = stk.pop()
    D = depth[a]

    for p,d in adj[a]:
        if depth[p]:
            continue
        parent[p] = a
        dist[p] = d
        stk.append(p)
        depth[p] = D+1

parent = [parent]
dist = [dist]

flag = 1

while True:
    flag = 0
    pcnt = [0]
    dcnt = [0]
    for i in range(1,N+1):
        pp = parent[-1][i] #parent
        ppp = parent[-1][pp]
        pcnt.append(ppp)
        dcnt.append(dist[-1][i]+dist[-1][pp])
        flag = max(flag,ppp)
    if flag:
        parent.append(pcnt)
        dist.append(dcnt)
    else:
        break
L = len(dist)
for _ in range(int(input())):
    a = map(int,input().split())
    if next(a) == 1:
        u,v = a
        rst = 0
        if depth[u]<depth[v]:
            u,v = v,u #u가 올라가야함
        diff = depth[u] - depth[v]
        for i in range(L):
            if (1<<i)&diff:
                rst += dist[i][u]
                u = parent[i][u]
        for i in range(L-1,-1,-1):
            if parent[i][u] != parent[i][v]:
                rst += dist[i][u]+dist[i][v]
                u, v = parent[i][u], parent[i][v]
        if u!=v:

            rst += dist[0][u]+dist[0][v]
        print(rst)
        

    else:
        u,v,k = a
        k -= 1
        uu, vv = sorted((u,v), key = lambda x: depth[x])
        #vv가 올라가야함
        diff = depth[vv] - depth[uu]
        for i in range(L):
            if (1<<i)&diff:
                vv = parent[i][vv]
        for i in range(L-1,-1,-1):
            if parent[i][uu] != parent[i][vv]:
                uu, vv = parent[i][uu], parent[i][vv]
        if uu != vv:
            LCA = parent[0][uu]
        else:
            LCA = uu
        D1 = depth[u] - depth[LCA] #올라갈 거리
        D2 = depth[v] - depth[LCA] #내려갈 거리
        if D1>=k:
            for i in range(L):
                if (1<<i)&k:
                    u = parent[i][u]
            print(u)
        else:
            D2 = D1+D2-k
            for i in range(L):
                if (1<<i)&D2:
                    v = parent[i][v]
            print(v)
