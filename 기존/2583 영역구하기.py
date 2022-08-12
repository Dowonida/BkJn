M,N,K=map(int,input().split())

Map=[[1]*(N+2)]
for i in range(M):
    Map.append([1]+[0]*N+[1])
Map.append([1]*(N+2))
#Map이 visited


for i in range(K):
    a,b,c,d=map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            Map[k+1][j+1]=1
rst=sum((sum(Map[i][1:-1]) for i in range(1,M+1)))
#방문한 지점 수

RST=[]#지역별 영토 크기
vec=((-1,0),(1,0),(0,-1),(0,1))

while rst<M*N:
    #빈칸 찾기 
    for i in range(1,M+1):
        for j in range(1,N+1):
            if Map[i][j]==0:
                start=(i,j)
                Map[i][j]=1
                
                break
        else:
            continue
        break
    que=[start]


    #DFS돌리기
    cnt=1
    while que:
        R,C=que.pop()
        for dR,dC in vec:
            nR,nC=R+dR,C+dC
            if Map[nR][nC]==0:

                cnt+=1
                Map[nR][nC]=1
                que.append((nR,nC))
    RST.append(cnt)
    rst+=cnt

print(len(RST))
RST.sort()
print(*RST)
