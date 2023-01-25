import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input()) #노드의 수

adj = [ [] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)


#재귀로 돌릴 때 visited 없는 dfs가 가능한데
#반복문으로도 해보자.

sons = [0]*(N+1)
nidx = [0]*(N+1)
stk= [0,1]
parent = [0] *(N+1)
depth = [0]*(N+1)
depth[1] = 1
cent_p = [0]*(N+1) #센트로이드부모
while stk:
    cur = stk[-1]

    if nidx[cur] == len(adj[cur]):
        sons[cur] += 1 #자신
        stk.pop()

    else:
        nxt = adj[cur][nidx[cur]]
        if nxt == stk[-2]:
            nidx[cur] += 1
        elif sons[nxt]:
            sons[cur] += sons[nxt]
            nidx[cur] += 1
        else:
            stk.append(nxt)
            parent[nxt] = cur
            depth[nxt] = depth[cur] + 1

parent = [parent]
flag = 1
while flag:
    flag = 0
    pcnt = []
    for i in range(N+1):
        pp = parent[-1][parent[-1][i]]
        pcnt.append(pp)
        flag = max(flag,pp)
    if flag:
        parent.append(pcnt)
LP = len(parent)
stk = [1]

while stk:
    cur = stk.pop()
    snum = sons[cur] #이번 서브트리에서 처리할 전체 노드 수
    pcp = cent_p[cur]
    while True:

        for nxt in adj[cur]:
            if sons[nxt]>snum:
                continue
            if sons[nxt]>snum//2:
                sons[cur] -= sons[nxt]
                sons[nxt] = snum
                cent_p[nxt] = pcp
                cur = nxt
                break
        else: #cur이 이번 루트로 당첨 
            break

    
    for nxt in adj[cur]:
        if sons[nxt]>snum:
            continue
        cent_p[nxt] = cur
        stk.append(nxt)

Max = 200000 #최대 거리
is_white = {0}
white = [ [(Max,0)] for _ in range(N+1)] #거리,노드
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a== 1:
        if b in is_white:
            is_white.remove(b)
        else:
            is_white.add(b)
            cur = b
            while cur: #b가 더 깊다.
                dcur, db = cur, b #거리구하기 위한 임시 값
                if depth[cur]>depth[b]:
                    dcur, db = db, dcur
                diff = depth[db] - depth[dcur]
                for i in range(LP):
                    if diff&(1<<i):
                        db = parent[i][db]
                for i in range(LP-1,-1,-1):
                    if parent[i][db] != parent[i][dcur]:
                        db, dcur = parent[i][db], parent[i][dcur]
                if db!= dcur:
                    db = parent[0][db]
                D = depth[b] + depth[cur] - 2*depth[db]

                heappush(white[cur],(D,b))
                cur = cent_p[cur]
    else:
        rst = Max
        cur = b
        while cur:
            dcur, db = cur, b
            if depth[cur]>depth[b]:
                dcur, db = db, dcur
            diff = depth[db] - depth[dcur]
            for i in range(LP):
                if diff&(1<<i):
                    db = parent[i][db]
            for i in range(LP-1,-1,-1):
                if parent[i][db] != parent[i][dcur]:
                    db, dcur = parent[i][db], parent[i][dcur]
            if db != dcur:
                db = parent[0][db]
            D = depth[b] + depth[cur] - 2*depth[db]

            while white[cur][0][1] not in is_white:
                heappop(white[cur])

            rst = min(rst, D+white[cur][0][0])
            cur = cent_p[cur]
        if rst == Max:
            print(-1)
        else:
            print(rst)
            

