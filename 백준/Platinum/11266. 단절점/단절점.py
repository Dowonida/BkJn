import sys
input = sys.stdin.readline

V, E = map(int,input().split()) #점, 선

adj = [ [] for _ in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())
    adj[a].append(b) #a->b로 갈 수 있다.
    adj[b].append(a)

#DFS스패닝트리 만든 후, 내 자식 중에서, 나보다 빠르지 않은 자식이
#'하나라도' 있으면 단절점임
    
#단절점이 아니라고 가정하자. 
#그럼 꼭 내가 없어도 연결이 된다는 말임.
#그럼 내 모든 자식이 (나 없이도) 내 부모와 연결이 된다는 말임
#따라서 명제의 대우가 증명 

#루트노드의 경우 당연히 더 빠른 자식은 없음
#하지만, 자식이 하나뿐일 경우 단절은 못시킴. 따라서 특수케이스로
#자식 둘이 필요함

    
#따라서, 리프노드는 모두 단절점이 될 수 없음
#자식 자체가 없기 때문.
#자식이 둘인데, 하나는 나보다 빠르고 하나는 느리다? 단절점임

#dfs 돌면서 노드에 번호를 매겨줌
#더 이상 방문할 곳이 없으면
#부모노드의 단절 여부를 체크하고,
#인접 노드 중 가장 작은 값을 자신의 값으로 가져오고 스택에서 팝
#연결그래프가 아닐 수도 있으므로, visited값이 다 채워질 때까지
#반복 DFS

#정식 DFS를 해야해서 조금 번거롭긴 함 
rst = [0]*(V+1) #단절여부
visited = [0]*(V+1)

for i in range(1,V+1):
    if visited[i]:
        continue
    visited[i] = 1
    stk = [i]
    cnt = 0 #루트의 자식 수 
    while stk:
        a = stk[-1]

        for b in adj[a]:
            if visited[b] == 0:
                visited[b] = visited[a]+1
                stk.append(b)
                cnt += (a==i)
                break
        else:
            if len(stk)>1:
                p = stk[-2]
                for b in adj[a]:
                    visited[a] = min (visited[a],visited[b])
                if visited[a]>=visited[p]:
                    rst[p] = 1
            stk.pop()
        #print(a,visited,stk)
        rst[i] = int(cnt>1)

        
RST = []
for i in range(1,V+1):
    if rst[i]:
        RST.append(i)
print(len(RST))
print(*RST)
