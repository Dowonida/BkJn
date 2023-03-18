import sys
input = sys.stdin.readline

N = int(input())
adj = [ [] for _ in range(N)]

for a in range(1,N):
    b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))


parent = [0]*N+[N]
dist = [0]*N+[0]
depth = [0]*N #visited를 겸함
depth[0] = 1
parent[0] = N #임시.
sons = [1]*(N+1)
stk = [0]
lst_idx = [0]*N #마지막으로 방문한 인덱스
cent_s = [set() for _ in range(N+1)]
cent_s[-1].add(0)

while stk:
    cur = stk[-1]
    
    cur_d = depth[cur]
    while lst_idx[cur]<len(adj[cur]):
        
    
        if depth[adj[cur][lst_idx[cur]][0]]:
            lst_idx[cur]+=1
            continue
        #다음 점을 뽑았음
        p, d = adj[cur][lst_idx[cur]]
        parent[p] = cur
        dist[p] = d
        cent_s[cur].add(p)
        depth[p] = cur_d+1
        stk.append(p)
        break
    else:
        #다 돌았음
        sons[parent[cur]] += sons[cur]
        stk.pop()

sons.pop()
cent_p = parent.copy()
stk = [cur]
while stk:
    cur = stk.pop()
    while True:
        pp = cent_p[cur]
        for son in cent_s[cur]:
            if sons[son]*2>sons[cur]:
                cent_p[son], cent_p[cur] = pp, son
                sons[cur], sons[son] = sons[cur]-sons[son], sons[cur]
                cent_s[cur].remove(son)
                cent_s[son].add(cur)
                cent_s[pp].remove(cur)
                cent_s[pp].add(son)
                cur = son
                break
        else:
            for son in cent_s[cur]:
                stk.append(son)
            break

parent = [parent]
dist = [dist]
while True:
    recent_p = parent[-1]
    recent_d = dist[-1]
    new_p = [0]*N+[N]
    new_d = [0]*N+[0]
    for i in range(N):
        p = recent_p[i]
        new_p[i] = recent_p[p]
        new_d[i] = recent_d[p]+recent_d[i]
    if min(new_p)<N:
        parent.append(new_p)
        dist.append(new_d)
    else:
        break


def Dist(a,b):
    if depth[a]>depth[b]:
        a,b = b,a #b가 더 깊음

    rst = 0
    diff = depth[b]-depth[a]
    for i in range(len(parent)):
        if diff&(1<<i):
            rst += dist[i][b]
            b = parent[i][b]

    if a!=b:
        for i in range(len(parent)-1,-1,-1):
            pa = parent[i][a]
            pb = parent[i][b]
            if pa!=pb:
                rst += dist[i][a]+dist[i][b]
                a,b = pa,pb
    
        rst+=dist[0][a]+dist[0][b]
    return rst

blue_dist = [{i:0 for i in cent_s[j]} for j in range(N)]
blue_count = [{i:0 for i in cent_s[j]} for j in range(N)]
isblue = set()
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        if b in isblue:
            continue
        isblue.add(b)
        cur = cent_p[b]
        prev = b
        while cur<N:
            blue_dist[cur][prev] += Dist(cur,b)
            blue_count[cur][prev] += 1
            prev = cur
            cur = cent_p[cur]
    else:
        rst = 0
        for i in blue_dist[b]:
            rst += blue_dist[b][i]
        cur = cent_p[b]
        prev = b
        while cur<N:
            D = Dist(cur,b)
            cnt = 0
            for i in blue_dist[cur]:
                if i == prev:
                    continue
                rst += blue_dist[cur][i]
                cnt += blue_count[cur][i]
            rst += cnt*D
            rst += (cur in isblue)*D
                

            prev = cur
            cur = cent_p[cur]
        print(rst)