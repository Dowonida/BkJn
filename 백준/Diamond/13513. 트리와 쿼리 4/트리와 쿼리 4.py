import sys
input = sys.stdin.readline
from heapq import heappop, heappush
#서브트리 내에서의 답을 저장만 하고
#조회할 때 처리 
def getDist(a,b):
    if depth[a]<depth[b]:
        a,b = b,a #a가 더 깊음
    diff = depth[a]- depth[b]
    rst = 0
    for i in range(LP):
        if diff&(1<<i):
            rst += dist[i][a]
            a = parent[i][a]

    for i in range(LP-1,-1,-1):
        if parent[i][a] != parent[i][b]:
            rst += dist[i][a] + dist[i][b]
            a, b = parent[i][a], parent[i][b]
    if a!=b:
        rst += dist[0][a]+dist[0][b]
    return rst
    
N = int(input()) #노드의 수
Max = 2000000000

Answer = [0]*(N+1) #현재의 답
white = [1]*(N+1)
adj = [ [] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int,input().split())
    adj[a].append((b,-c))
    adj[b].append((a,-c)) #최소구할거임 마지막에만 -붙여서 출력 


#재귀로 돌릴 때 visited 없는 dfs가 가능한데
#반복문으로도 해보자.

sons = [0]*(N+1)
nidx = [0]*(N+1)
stk= [0,1]
parent = [0] *(N+1)
dist = [0]*(N+1)
depth = [0]*(N+1)
depth[1] = 1


while stk:
    cur = stk[-1]

    if nidx[cur] == len(adj[cur]):
        sons[cur] += 1 #자신
        stk.pop()

    else:
        nxt,d = adj[cur][nidx[cur]]
        if nxt == stk[-2]:
            nidx[cur] += 1
        elif sons[nxt]:
            sons[cur] += sons[nxt]
            nidx[cur] += 1
        else:
            stk.append(nxt)
            parent[nxt] = cur
            dist[nxt] = d
            depth[nxt] = depth[cur] + 1

parent = [parent]
dist = [dist]
flag = 1
while flag:
    flag = 0
    pcnt = []
    dcnt = []
    for i in range(N+1):
        p = parent[-1][i]
        pp = parent[-1][p]
        pcnt.append(pp)
        dcnt.append( dist[-1][i]+dist[-1][p])
        flag = max(flag,pp)
    if flag:
        parent.append(pcnt)
        dist.append(dcnt)
LP = len(parent)


stk = [1]
nidx = [0]*(N+1)
is_cented = [0]*(N+1)

cent_p = [0]*(N+1) #센트로이드 부모

cent_s = [ {i:[(0,i)]} for i in range(N+1)] #내 직계자식: 힙 
cent_ss = [ {i:{i:1}} for i in range(N+1)] #i번 힙안에 i가 1개 있다
#지우는 경우 -> radius 체크해서 유효할 때만 업데이트
#추가하는 경우 cent_ss 체크해서 없는 경우에만 업데이트

while stk:
    
    cur = stk[-1]

    snum = sons[cur]
    cpp = cent_p[cur]
    while True:

        for i,d in adj[cur]:
            if is_cented[i]:
                continue
            if sons[i]>sons[cur]//2:
                sons[cur] -= sons[i]
                sons[i] = snum
                cur = i
                break
        
        else:
            is_cented[cur] = 1
            cent_p[cur] = cpp
            #cent_s[cpp][cur] = []

            break
        stk[-1] = cur
    
    if is_cented[cur]: #내가 센터인게 확실하면
        #nidx비교 시작
        if nidx[cur] < len(adj[cur]):
            nxt,d = adj[cur][nidx[cur]]
            if is_cented[nxt]: #처리되었단 뜻임 부모일수도 
                nidx[cur] += 1
            else:
                stk.append(nxt)
                cent_p[nxt] = cur
                
            
            
        else:
            #부모한테 올려 줌 

            cent_s[cpp][cur] = [ ]
            cent_ss[cpp][cur] = {}
            for ss in cent_s[cur]:
                for d,p in cent_s[cur][ss]:
                    heappush(cent_s[cpp][cur], (getDist(cpp,p),p))
                    cent_ss[cpp][cur][p] = 1
            stk.pop()
        

radius = [ (i,i) for i in range(N+1)]
Answer[0] = Max
def updateAnswer(node):
    rst = []
    for i in cent_s[node]:
        while cent_s[node][i] and white[cent_s[node][i][0][1]] == 0:
            p=heappop(cent_s[node][i])[1]
            cent_ss[node][i][p]=0
        if cent_s[node][i]:
            rst.append(cent_s[node][i][0])

        rst = sorted(rst)[:2]
    if len(rst)==0:
        Answer[node] = Max
    elif len(rst)==1:
        Answer[node] = 0
    else:
        Answer[node] = rst[0][0]+rst[1][0]
        radius[node] = (rst[0][1],rst[1][1]) #양 끝 

for i in range(1,N+1):
    updateAnswer(i)
        


for _ in range(int(input())):
    A = map(int,input().split())
    if next(A) == 1:
        a, = A
        white[a] = 1-white[a]
        
        if white[a]:
            
            if cent_ss[a][a][a] == 0:
                cent_ss[a][a][a] = 1
                heappush(cent_s[a][a],(0,a))
            cur = a
            p = cent_p[cur]
            
            

            while p:
                if cent_ss[p][cur][a] == 0:
                    cent_ss[p][cur][a] = 1
                    heappush(cent_s[p][cur], (getDist(p,a),a))
                    updateAnswer(p)
                p = cent_p[p]
                cur = cent_p[cur]
        else:
            cur = a
            while cur:
                if a in radius[cur]:
                    updateAnswer(cur)
                cur = cent_p[cur]


    else:
        rst = min(Answer)
        if rst == Max:
            print(-1)
        else:
            print(-rst)
