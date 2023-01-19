import sys
input = sys.stdin.readline

N, M = map(int,input().split())

adj = [ set() for _ in range(2*N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    adj[-a].add(b)
    adj[-b].add(a)


visited = [0]*(2*N+1)
finished = [0]*(2*N+1)
finished[0] = 1
SCC = []

for i in range(-N,N+1):
    if finished[i]:
        continue

    visited[i] = 1
    cnt = 1
    stk = [i]
    cur = i #현재 포인터

    while stk:
        
        Min = visited[cur]
        nxt = cur
        for you in adj[cur]:
            if visited[you] == 0:
                stk.append(you)
                cur = you
                cnt += 1
                visited[you] = cnt
                
                break
            elif finished[you]==0:
                if visited[you] < visited[nxt]:
                    Min = visited[you]
                    nxt = you

        else:
            if nxt == cur:
                scc = set()
                while stk[-1]!=cur:
                    scc_e = stk.pop()
                    scc.add(scc_e)
                    finished[scc_e] = 1
                scc_e = stk.pop()
                scc.add(scc_e)
                finished[scc_e] = 1
                SCC.append(scc)
                if stk:
                    cur = stk[-1]
                
            else:
                cur = nxt

for scc in SCC:
    for i in scc:
        if -i in scc:
            print(0)
            break
    else:
        continue
    break
else:
    print(1)

                
