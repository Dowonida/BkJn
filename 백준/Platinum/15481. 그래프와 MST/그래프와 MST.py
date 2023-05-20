import sys
sys.setrecursionlimit(210000)
input = sys.stdin.readline

N, M = map(int,input().split())
'''
로직
최소 갱신트리 일단 만들고 가중치 합 저장
조상까지의 거리를 저장
def dist = max(a,b경로상의 가중치)
a,b를 잇는 가중치 w간선이 주어지면
mst가중치+w-dist(a,b)

mst만들기
거리 저장
계산 

'''
U=list(range(N+1)) #대표노드
E = [ tuple(map(int,input().split())) for _ in range(M)] #간선 리스트
def find(a):
    if a != U[a]:
        a = find(U[a])
    return U[a]

def union(a,b):
    a,b = sorted([find(a),find(b)])
    if a==b:
        return False
    else:
        U[b] = a
        return True

S = 0
adj = [ [] for _ in range(N+1)]
for a,b,w in sorted(E, key = lambda x: x[2]):
    if union(a,b):
        adj[a].append((b,w))
        adj[b].append((a,w))
        S += w
    
parent = [0]*(N+1)
dist = [0]*(N+1) #부모까지 가는 거리
depth = [0]*(N+1)
depth[1] = 1

stk=[1]
while stk:
    cur = stk.pop()
    nxt_dep = depth[cur]+1
    for nxt,d in adj[cur]:
        if depth[nxt]:
            continue
        parent[nxt] = cur
        dist[nxt] = d
        depth[nxt] = nxt_dep
        stk.append(nxt)
    
md = max(depth).bit_length()-1

parent = [parent]
dist = [dist]
for i in range(md):
    p_cnt = [0]*(N+1)
    d_cnt = [0]*(N+1)
    for j in range(2,N+1):
        my_parent = parent[-1][j]
        p_cnt[j] = parent[-1][my_parent]
        d_cnt[j] = max(dist[-1][j],dist[-1][my_parent])
    parent.append(p_cnt)
    dist.append(d_cnt)

for a,b,w in E:
    if depth[a]>depth[b]:
        a,b = b,a
        #b가 더 깊다.-> 더 올라가야 한다.

    diff = 0
    dep_diff = depth[b]-depth[a]
    for i in range(dep_diff.bit_length()):
        if dep_diff&(1<<i):
            diff = max(diff, dist[i][b])
            b = parent[i][b]

    for i in range(md,-1,-1):
        na, nb = parent[i][a], parent[i][b]
        if na!=nb:
            diff = max(diff, dist[i][a], dist[i][b])
            a,b = na,nb
    if a!=b:
        diff = max(diff,dist[0][a], dist[0][b])

    print(S+w-diff)
        
            
    







    
