N=int(input())
L=[ list(map(int,input())) for _ in range(N)]

#이상의 가격으로 1번만 
stack=[ (0,1,0)] #최근 사람 번호, 지금까지방문한 사람들, 가격
rst=0
visited=[[10]*(1<<N) for _ in range(N)]
while stack:
    #print(stack)
    me,V,P = stack.pop()
    cnt=0
    for i in range(N):
        if V & (1<<i):
            cnt+=1
        elif L[me][i]>=P:
            v=V+(1<<i)
            if visited[i][v]>L[me][i]:
                visited[i][v]=L[me][i]
                
                stack.append((i,v,L[me][i]))
            
            pass
    rst=max(rst,cnt)
    if rst==N:
        break

print(rst)
