import sys
input=sys.stdin.readline


M, N = map(int,input().split())
Map=[[2]*(N+2)]

for i in range(M):
    Map.append([2]+list(map(int,list(input().strip())))+[2])
Map.append([2]*(N+2))

visited=[[0]*(N+2) for i in range(M+2)]
visited[1][1]=2
#미방문 0
#망치방문 1
#그냥방문 2 => 망치보다 작은 값이면 망치값으로 변경


cnt=1
que=[(1,1,2)]#2가 망치 있는거=>1인 벽을 부술 수 있음 
vector=[(-1,0),(1,0),(0,1),(0,-1)]
while visited[M][N]==0 and que:

    nextque=[]
    for i in range(len(que)):
        for j in vector:
            nx,ny=que[i][0]+j[0],que[i][1]+j[1]#다음 좌표
            if visited[nx][ny]<que[i][2] and Map[nx][ny]<que[i][2]:#갈 수 있으면
                visited[nx][ny]=que[i][2]
                nextque.append((nx,ny,que[i][2]-Map[nx][ny]))

    que=nextque
    cnt+=1
if visited[-2][-2]==0:
    print(-1)
else:
    print(cnt)
