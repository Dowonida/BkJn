import sys
input = sys.stdin.readline
#각 간선마다 위로 노드 수, 밑으로 노드 수
#위 노드 수 * 아래 노드 수 + 아래 노드수C2 를 전부 더하면 됨

#트리 구축 후
#각 노드별로 자식 노드 수를 저장함

#계산을 부모에서할까 자식에서 할까
#자식에서 계산하는 장점: 계산할 간선(부모로 가는것)이 유일함
#간선 내부의 수랑 외부의 수를 바로 구할 수 있음
#내부: 자식노드의 자손 수, 외부: N- 나의 자손

#트리 구축+자식 저장에 DFS한번 O(N)
#각 노드별 계산에 O(N)

N = int(input())
adj = [ [] for _ in range(N+1)]
sons = [1]*(N+1)
parent = [0]*(N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

stk = [1]
stk2 = []
#리프노드까지 부모 저장하며 내려감
#루트노드까지 부모에 더해주며 올라옴

parent[1]= 1

while stk:
    me = stk.pop()
    leaf = True
    for i in adj[me]:
        
        if parent[i]:
            continue
        leaf = False
        parent[i] = me
        stk.append(i)
    if leaf:
        stk2.append(me)
    

visited = [1]*(N+1)
while stk2:

    i = stk2.pop()
    p = parent[i]
    if visited[i] == len(adj[i]):
        sons[p] += sons[i]
        visited[p] += 1
        stk2.append(p)





rst = 0
for i in range(2,N+1):
    inner = sons[i]
    outer = N-inner
    rst += inner*outer + (inner*(inner-1))//2
print(rst)

