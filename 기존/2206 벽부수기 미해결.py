import sys
input=sys.stdin.readline

N,M=map(int,input().split())
Map=[]
for i in range(N):
    Map.append(list(map(int,list(input().strip()))))

que=[(0,0,1)]#x,y,망치 
visited={}
cnt=1
while que:

    for i in range(len(que)):
        
        x,y,m=que.pop(0)#좌표와 망치
        if x<0 or x>=M or y<0 or y>=N or (x,y,m) in visited:
            continue
        if Map[y][x]==1 and m==0:
            visited[(x,y,m)]=cnt
            continue
        if Map[y][x]==1:
            m=0
        visited[(x,y,m)]=cnt #망치 있는거랑 없는거 따로 저장
        
        que+=[(x-1,y,m),(x+1,y,m),(x,y-1,m),(x,y+1,m)]
        print(que)
    cnt+=1
        
print(cnt,visited)


