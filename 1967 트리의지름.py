N=int(input())


dic={ i : {} for i in range(1,N+1)}
#점: {다른 점: 거리, 다른점2 : 거리2}
for i in range(N-1):
    a,b,c=map(int,input().split())
    dic[a][b]=c
    dic[b][a]=c


visited=[]
stack=[(1,0)]
dist=0
far=1
while stack:
    n,d=stack.pop()
    if n not in visited:
        visited.append(n)
        for i in set(dic[n])-set(visited):
            stack.append((i,d+dic[n][i]))
            if d+dic[n][i]>dist:
                far=i
                dist=d+dic[n][i]
                
visited=[]
stack=[(far,0)]
dist=0
while stack:
    n,d=stack.pop()
    if n not in visited:
        visited.append(n)
        for i in set(dic[n])-set(visited):
            stack.append((i,d+dic[n][i]))
            if d+dic[n][i]>dist:
                far=i
                dist=d+dic[n][i]

print(dist)
