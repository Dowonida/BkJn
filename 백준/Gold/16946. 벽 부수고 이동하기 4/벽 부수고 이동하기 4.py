import sys
input=sys.stdin.readline

R,C=map(int,input().split())

Map=[[1]*(C+2)]
for i in range(R):
    Map.append([1]+list(map(int,input().strip()))+[1])
Map.append([1]*(C+2))
dic={1:0}#영역번호별로 영역크기 저장 
#이후에 인접한 영역번호를 set으로 합친다음
#set안의 원소들의 키 즉 영역의 넓이를 합할거임 
cnt=2
for r in range(1,R+1):
    for c in range(1,C+1):
        if Map[r][c]==0:
            que=[(r,c)]
            Map[r][c]=cnt
            dic[cnt]=1
            while que:
                rr,cc=que.pop()
                if Map[rr-1][cc]==0:
                    que.append((rr-1,cc))
                    Map[rr-1][cc]=cnt
                    dic[cnt]+=1
                    
                if Map[rr+1][cc]==0:
                    que.append((rr+1,cc))
                    Map[rr+1][cc]=cnt
                    dic[cnt]+=1
                    
                if Map[rr][cc-1]==0:
                    que.append((rr,cc-1))
                    Map[rr][cc-1]=cnt
                    dic[cnt]+=1
                    
                if Map[rr][cc+1]==0:
                    que.append((rr,cc+1))
                    Map[rr][cc+1]=cnt
                    dic[cnt]+=1
            cnt+=1
                
            
for r in range(1,R+1):
    rst=''
    for c in range(1,C+1):
        if Map[r][c]==1:
            S=set()
            S.add(Map[r-1][c])
            S.add(Map[r+1][c])
            S.add(Map[r][c-1])
            S.add(Map[r][c+1])
            cnt=1
            for i in S:
                cnt+=dic[i]
            rst+=str(cnt%10)
        else:
            rst+='0'
    print(rst)
