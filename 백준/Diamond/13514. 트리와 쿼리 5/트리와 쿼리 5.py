import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(200000)


N = int(input())
parent = [0]*(N+1)
sonnum = [0]*(N+1)
depth = [0]*(N+1)

sons = [ set() for _ in range(N+1)]
adj = [ [] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)


def upson(node = 1, d=1):
    sonnum[node] = 1
    depth[node] = d

    for i in adj[node]:
        if sonnum[i]:
            continue
        sons[node].add(i)
        parent[i] = node
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
violins = {0}
Violin = [[(Max,0)] for _ in range(N+1)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a== 1:
        if b in violins:
            violins.remove(b)
            continue
        violins.add(b)
        cur = b
        while cur:
            heappush( Violin[cur], ( dist(cur,b),b))
            cur = centp[cur]
        
    else:
        rst = Max
        cur = b
        while cur:
            while Violin[cur][0][1] not in violins:
                heappop(Violin[cur])
            rst = min(rst, Violin[cur][0][0]+dist(cur,b))
            cur = centp[cur]

        if rst == Max:
            print(-1)
        else:
            print(rst)
        
        
    
