import sys
input=sys.stdin.readline


M, N, K = map(int,input().split())
Map=[[K+1]*(N+2)]

for i in range(M):
    Map.append([K+1]+list(map(int,list(input().strip())))+[K+1])
Map.append([K+1]*(N+2))

visited=[[0]*(N+2) for i in range(M+2)]
visited[1][1]=2
#미방문 0
#망치방문 1
#그냥방문 2 => 망치보다 작은 값이면 망치값으로 변경


cnt=1
day=1
que={(1,1,K+1)}#2가 망치 있는거=>1인 벽을 부술 수 있음 
vector=[(-1,0),(1,0),(0,1),(0,-1)]
while visited[M][N]==0 and que:

    nextque=set()
    for i in que:
        for j in vector:
            nx,ny=i[0]+j[0],i[1]+j[1]#다음 좌표
            if visited[nx][ny]<i[2] and Map[nx][ny]==0:#벽 없으면
                visited[nx][ny]=i[2]
                nextque.add((nx,ny,i[2]-Map[nx][ny]))
            elif visited[nx][ny]<i[2] and Map[nx][ny]<i[2]:#갈 수 있는데 벽이면
                if day==1:
                    visited[nx][ny]=i[2]
                    nextque.add((nx,ny,i[2]-1))
                else:
                    nextque.add((i))
    que=nextque
    cnt+=1
    day*=-1
if visited[-2][-2]==0:
    print(-1)
else:
    print(cnt)
