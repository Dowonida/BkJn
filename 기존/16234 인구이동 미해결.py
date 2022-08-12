N,Min,Max=map(int,input().split())

Map=[[-200]*(N+2)]
for i in range(N):
    Map.append([-200]+list(map(int,input().split()))+[-200])
Map.append([-200]*(N+2))
#Map이 visited
#간섭받지 않는 -200을 줌 


visited=[[1]*(N+2)]
for i in range(N):
    visited.append([1]+[0]*N+[1])
    
visited.append([1]*(N+2)) #방문지점 셋팅
#이후 복사해서 쓰기
#그냥 방문지점값이 n**2면 나오자 
vec=((-1,0),(1,0),(0,-1),(0,1))

turn=0
while True:
    V=[]
    for i in visited:
        V.append(i.copy())
    RST=[]#동맹국 리스트

#------------------------------------------동맹국 묶기 과정 --------------------------------------
    exit1=0#while탈출 숫자
    #visited를 다 채우면 탈출 즉 exit가 N*N이면 탈출

    #------------------------------------------시작점 선택 과정--------------------------------------
    while exit1<N*N:
        #빈칸 찾기-시작점 
        for i in range(1,N+1):
            for j in range(1,N+1):
                if V[i][j]==0:
                    start=(i,j)
                    V[i][j]=1
                    
                    break
            else:
                continue
            break
        que=[start]
    #------------------------------------------영역 묶기과정--------------------------------------
        #DFS돌리기
        cnt=[start]#이번 영역 
        while que:
            R,C=que.pop()
            exit1+=1
            for dR,dC in vec:
                nR,nC=R+dR,C+dC
                #------------------------------------------인구확인 과정 --------------------------------------
                if V[nR][nC]==0 and Min<=abs(Map[R][C]-Map[nR][nC])<=Max:
                    cnt.append((nR,nC))#영역합치기
                    V[nR][nC]=1#방문처리
                    que.append((nR,nC))#다음 큐에 추가

        #cnt가 영역완료 됨 
        RST.append(cnt)#동맹 추가
        
    #------------------------------------------인구이동과정--------------------------------------          
    if len(RST)==N*N:
        break
    for i in RST:
        average=sum([Map[k[0]][k[1]] for k in i])//len(i)
        for r,c in i:
            Map[r][c]=average
    turn+=1




    


print(turn)
