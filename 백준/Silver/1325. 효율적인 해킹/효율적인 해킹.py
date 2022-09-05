N, M= map(int,input().split())

cnt=0
dic={i:set() for i in range(1,N+1)}
for i in range(M):
    a, b = map(int,input().split())
    dic[b].add(a)


for i in range(1,N+1):
    visited=[0]*(N+1)
    visited[i]=1
    stack=[i]
    
    while stack:
        a = stack.pop()
        for j in dic[a]:
            if visited[j]==0:
                visited[j]=1
                stack.append(j)
    R = sum(visited)
    if R>cnt:
        cnt=R
        rst=[i]
    elif R==cnt:
        rst.append(i)
print(*rst)
    
    
