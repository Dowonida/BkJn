import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

N, C = map(int,input().split())

adj = [ [] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)


depth = [0]*(N+1)
cnt = N #방문순서이자 세그먼트 인덱스 
depth[C] = 1
parent = [0]*(N+1)
seg_idx = [0]*(N+1) #세그먼트에서 몇번째인지
seg_idx[C] = N
last_idx = [0]*(N+1) #내 서브트리에서 마지막 방문 번호
last_idx[C] = N
n_idx =[0]*(N+1) #마지막 처리 번호 
stk = [C]

while stk:
    cur = stk[-1]
    if n_idx[cur]<len(adj[cur]):
        nxt = adj[cur][n_idx[cur]]
        n_idx[cur] += 1
        if depth[nxt]:
            continue
        stk.append(nxt)
        parent[nxt] = cur
        depth[nxt] = depth[cur]+1
        cnt += 1
        seg_idx[nxt] = cnt
        last_idx[nxt] = cnt
    else:
        last_idx[parent[cur]] = last_idx[cur]
        stk.pop()
    
seg = [0]*2*N
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a== 1:
        idx = seg_idx[b]
        while idx:
            seg[idx] += 1
            idx //= 2
    else:
        s,e = seg_idx[b], last_idx[b]+1
        rst = 0
        while s<e:
            if s%2:
                rst += seg[s]
                s += 1
            if e%2:
                e -= 1
                rst += seg[e]
            s//=2
            e//=2
        print(rst*depth[b])
