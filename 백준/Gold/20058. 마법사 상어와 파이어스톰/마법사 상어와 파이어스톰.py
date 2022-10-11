import sys
input=sys.stdin.readline


N,M=map(int,input().split())
NN=1<<N
Map=[[0]*(2+(NN))]+[[0]+ list(map(int,input().split()))+[0] for _ in range(NN)]+[[0]*(2+(NN))]

def rotate(n):
    global Map
    
    #W= 1<<(N-n)#한 변에 작은 사각형 W개 
    w= 1<<n #작은 사각형의 한 변
    

    c=w//2+0.5
    cnt_Map=[ [0]*(2+NN) for _ in range( (2+NN))]
    #print(cnt_Map)
    for r in range(1,NN+1):
        absR= (r-1)//w*w 
        for c in range(1,NN+1):
            absC= (c-1)//w*w
            #기준점 print(baseR,baseC)
            relR, relC= (r-1)%w+1, (c-1)%w+1
            #print(relR,relC)
            cnt_Map[absR+relC][absC+w+1-relR]=Map[r][c]
    Map=cnt_Map
    Remove=[]
    for r in range(1,NN+1):
        for c in range(1,NN+1):
            if len( [ Map[x][y] for x,y in ( (r-1,c),(r+1,c),(r,c-1),(r,c+1)) if Map[x][y]])<3:
                Remove.append((r,c))
    for r,c in Remove:
        Map[r][c]=max(0,Map[r][c]-1)
            
            
    #print(cnt_Map)
            
            


for i in list(map(int,input().split())):
    rotate(i)

print( sum( [sum(i) for i in Map]))
    
visited=[ [0]*(2+NN) for _ in range( (2+NN))]
RST=0
for i in range(1,NN+1):
    for j in range(1,NN+1):
        if Map[i][j] and visited[i][j]==0:
            que=[(i,j)]
            visited[i][j]=1
            rst=1
            while que:
                nq=[]
                for r,c in que:
                    for nr,nc in ( (r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                        if Map[nr][nc] and visited[nr][nc]==0:
                            visited[nr][nc]=1
                            nq.append((nr,nc))
                            rst+=1

                que=nq
            RST=max(RST,rst)
print(RST)
