import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


N,M = map(int,input().split())
parent = [0,0]+ list(map(int,input().split()))
sonnum = [0]*(N+1)
depth = [0]*(N+1)

sons = [ set() for _ in range(N+1)]
for i in range(1,N+1):
    sons[ parent[i] ] .add(i)

def upson(node = 1, d=1):
    sonnum[node] = 1
    depth[node] = d

    for i in sons[node]:
        sonnum[node] += upson(i,d+1)

    return sonnum[node]

centp = [0]*(N+1)
upson()

def centing(node,p=0, ): #p는 이전센트

    snum = sonnum[node] #이번 서브트리 노드 수

    cent = node
    while True:

        for i in sons[cent]:
            if sonnum[i] > snum//2:
                

                sons[cent].remove(i)
                sons[i].add(cent)
                
                sonnum[cent] -= sonnum[i]
                sonnum[i] = snum
                cent = i
                break
        else:
            break

    centp[cent] = p
    for i in sons[cent]:
        centing(i,cent)

centing(1)

parent = [ parent]
Max = 1
while Max:
    Max = 0
    cnt = []
    for i in range(N+1):
        pp = parent[-1][parent[-1][i]]
        cnt.append(pp)
        Max = max(Max,pp)
    if Max:
        parent.append(cnt)
LP = len(parent)
def LCA(a,b):
    if depth[a]>depth[b]:
        a,b = b,a #b가 더 깊음
    diff = depth[b]-depth[a]
    for i in range(LP):
        if diff & (1<<i):
            b = parent[i][b]

    for i in range(LP-1,-1,-1):
        if parent[i][a] != parent[i][b]:
            a,b = parent[i][a], parent[i][b]
    if a!=b:
        return parent[0][a]
    return a

def dist(a,b):
    lca = LCA(a,b)
    return depth[a]+depth[b]- 2*depth[lca]

Max = 200000
Violin = [Max]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    if a== 1:
        cur = b
        while cur:
            Violin[cur] = min(Violin[cur],dist(cur,b))
            cur = centp[cur]
        
    else:
        rst = Max
        cur = b
        while cur:
            rst = min(rst, Violin[cur]+dist(cur,b))
            cur = centp[cur]

        if rst == Max:
            print(-1)
        else:
            print(rst)
        
        
    
