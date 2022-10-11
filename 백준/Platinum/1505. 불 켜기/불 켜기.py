R, C = map(int,input().split())

Map=[[0]*(C+2)]+[[0]+list(map(int,input().strip().replace('*','0').replace('.','1')))+[0] for _ in range(R)]+[[0]*(C+2)]
#눌러야되는 횟수 총합

start=[(1,j) for j in range(1,1+C)]+[(j,1) for j in range(2,1+R)]

end=[ (R,j) for j in range(1,C+1)]+[(j,C) for j in range(1,R)]
#print(start)
#print(end)
#가장자리 
rst=100
for i in range(1<<(R+C-1)):
    NMap=[ [0]*(C+2) for i in range(2+R)]
    cnt=0
    for j in range(R+C-1):
        if 1<<j & i:
            cnt+=1#버튼 누른 횟수 
            NMap[start[j][0]][start[j][1]]=1
    #print(NMap)
    for r in range(2,R+1):
        for c in range(2,C+1):

            on=(Map[r-1][c-1]+NMap[r-2][c-2]+NMap[r-2][c-1]+NMap[r-2][c]
                +NMap[r-1][c-2]+NMap[r-1][c-1]+NMap[r-1][c]
                +NMap[r][c-2]+NMap[r][c-1])%2
            NMap[r][c]=on
            cnt+=on
            if cnt>rst:
                break
        if cnt>rst:
            break
    #print(cnt)
    for r,c in end:
        if (Map[r][c]+NMap[r][c]+NMap[r-1][c-1]+NMap[r-1][c]+NMap[r-1][c+1]+
            NMap[r][c-1]+NMap[r][c+1]+NMap[r+1][c-1]+NMap[r+1][c]+NMap[r+1][c+1])%2:
            break
    else:
        rst=min(rst,cnt)

if rst==100:
    print(-1)
else:
    print(rst)
    
    
    
