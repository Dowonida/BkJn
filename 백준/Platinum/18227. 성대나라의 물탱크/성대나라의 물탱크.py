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
depth[C] = 1
#sons = [ [] for _ in range(N+1)] #자식노드 번호
sub_count = [1]*(N+1) #서브트리 크기 
chain_info = [0]*(N+1) #몇번 체인에 속하는지 (a,b꼴로 저장) a번체인 b번순서
chains = []
parent = [0]*(N+1)
#자식이 전부 처리되었으면 체인번호를 정한다.
#자식이 없다면 새 체인번호 부여,
#자식이 있다면 가장 큰 서브트리를 가지는 자식과 동일하게 부여

def dfs(node=C):
    sons_cnt = 0

    for i in adj[node]:
        if depth[i]:
            continue
        depth[i] = depth[node]+1
        parent[i] = node
        dfs(i)
        sub_count[node] += sub_count[i]
        if sub_count[i]>sons_cnt:
            sons_cnt = sub_count[i]
            chain_info[node] = (chain_info[i][0],chain_info[i][1]+1)

    if sons_cnt == 0:
        chain_info[node] = (len(chains),0)
        chains.append([])
    chains[chain_info[node][0]] += [0,0]
    chains[chain_info[node][0]][0] = parent[node], chain_info[node][1]+1
    #어차피 0번은 결번이니까 올라갈 노드번호, 체인길이를 저장 

dfs()
        
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        while b:
            chain, s = chain_info[b]
            seg=chains[chain]
            s += seg[0][1]
            e = seg[0][1]*2
            b = seg[0][0]

            while s<e:
                if s%2:
                    seg[s] += 1
                    s += 1
                if e%2:
                    e -= 1
                    seg[e] += 1
                s//=2
                e//=2
        continue
    else:
        chain, s = chain_info[b]
        seg=chains[chain]
        s += seg[0][1]
        rst = 0
        scale = depth[b]
        while s:
            rst += seg[s]*scale
            s//=2
        print(rst)

