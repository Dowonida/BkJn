import sys
input = sys.stdin.readline

N, M = map(int,input().split())

adj = [ [] for _ in range(2*N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    adj[-a].append(b)
    adj[-b].append(a)


visited = [0]*(2*N+1)
finished = [0]*(2*N+1)
finished[0] = 1
top = [0]*(2*N+1)
checked = [0]*(2*N+1)
SCC = []
previdx= [0]*(2*N+1)

TF = [0]*(2*N+1)
for i in range(-N,N+1):
    if finished[i]:
        continue

    visited[i] = 1
    cnt = 1
    stk = [i]
    idx = 0
    top[i] = cnt

    while stk:
        cur = stk[idx]
        
        if checked[cur]<len(adj[cur]):
        #for j in range(checked[cur],len(adj[cur])):
            you = adj[cur][checked[cur]]
        
            if visited[you] == 0:
                stk.append(you)
                previdx[you] = idx
                cur = you
                cnt += 1
                visited[you] = cnt
                top[you] = cnt
                idx = len(stk)-1
                
            else:
                checked[cur] += 1
                if finished[you] == 0:
                    
                    top[cur] = min(top[cur],top[you])
                    
        else: #더 방문할 곳이 없는 경우
            if top[cur] < visited[cur]: #더 올라갈 수 있다면
                idx = previdx[cur] #스택을 유지한채 한 칸 위로
            else:
                scc = set()
                tf = 1
                while True:
                    s = stk.pop()
                    tf = min(tf,1-TF[-s])
                    scc.add(s)
                    finished[s] = 1
                    if s == cur:
                        break
                for el in scc:
                    TF[el] = tf
                SCC.append(scc)
                idx = previdx[cur]
            


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
    for i in range(1,N+1):
        print(TF[i],end = ' ')

                
