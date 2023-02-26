import sys
input = sys.stdin.readline

N, C = map(int,input().split())

adj = [ [] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

depth = [0]*(N+1)
S_idx = [0]*(N+1)
E_idx = [0]*(N+1)
depth[C] = 1
cnt = N
S_idx[C] = N
E_idx[C] = N+1

stk = [C]
while stk:
    cur = stk[-1]
    if adj[cur]:
        nxt = adj[cur].pop()
        if depth[nxt]:
            continue
        cnt += 1
        S_idx[nxt] = cnt
        E_idx[nxt] = cnt+1
        depth[nxt] = depth[cur]+1
        stk.append(nxt)
    else:
        stk.pop()
        if stk:
            E_idx[stk[-1]] = E_idx[cur]
        

seg = [0]*2*N
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        idx=S_idx[b]
        while idx:
            seg[idx]+=1
            idx//=2
    else:
        rst =0
        s,e = S_idx[b], E_idx[b]
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
