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
sons = [0]*(N+1)
#parents = [0]*(N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

stk = [1]
# sons도 계산하기 위해서 DFS는 정석으로 돈다.
# 즉 한 번에 모든 자식을 추가하지 않고,
# 자식을 처리한 다음에 부모도 방문을 한다.
# 팝은 자식이 전부 처리된 이후에 한다.
# 이를 위해선 재귀함수가 좋다.
# 그럼 깊이는 30만.... 좀 슬프네

def DFS(node=1,parent=0):
    rst = 1
    #parents[node]=parent
    for i in adj[node]:
        if i == parent:
            continue
        rst += DFS(i,node)
    sons[node] = rst

    return rst

DFS(1)
rst = 0
for i in range(2,N+1):
    inner = sons[i]
    outer = N-inner
    rst += inner*outer + (inner*(inner-1))//2
print(rst)
