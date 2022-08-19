N=int(input())
T=int(input())
dic={i:[] for i in range(1,N+1)}
for i in range(T):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
    
que=[1]
visited=[0]*(N+1)
visited[1]=1
rst=0
while que:
    a=que.pop()
    for i in dic[a]:
        if visited[i]==0:
            visited[i]=1
            que.append(i)
            rst+=1
print(rst)
        