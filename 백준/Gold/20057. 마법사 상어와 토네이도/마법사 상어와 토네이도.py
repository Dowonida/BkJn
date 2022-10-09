N=int(input())
Vector=[ (0,-1),(1,0),(0,1),(-1,0)]

Map=[ [0]*(N+4) for i in range(N+4)]
for i in range(2,2+N):
    a=map(int,input().split())
    for j in range(2,2+N):
        Map[i][j]=next(a)

    
def move(r,c,v):
    dr,dc=Vector[v]
    vr,vc= 1-abs(dr),1-abs(dc) #수직인 방향 
    nr,nc=r+dr,c+dc             #다음 위치 
    sand=Map[nr][nc]           #분배할 모래 양 

    Map[nr][nc]=0
    Map[r+vr][c+vc]+=int(sand/100)
    Map[r-vr][c-vc]+=int(sand/100)
    Map[nr+vr][nc+vc]+=int(7*sand/100)
    Map[nr-vr][nc-vc]+=int(7*sand/100)
    Map[nr+2*vr][nc+2*vc]+=int(2*sand/100)
    Map[nr-2*vr][nc-2*vc]+=int(2*sand/100)

    Map[nr+dr+vr][nc+dc+vc]+=int(10*sand/100)
    Map[nr+dr-vr][nc+dc-vc]+=int(10*sand/100)

    Map[nr+2*dr][nc+2*dc]+=int(5*sand/100)

    Map[nr+dr][nc+dc]+=sand-2*(int(sand/100)+int(7*sand/100)+int(2*sand/100)
                                +int(10*sand/100))-int(5*sand/100)

v=0
r=c=N//2+2
turn=0
while True:
    move_count=turn//2+1
    v=turn%4
    for i in range(move_count):
        move(r,c,v)
        r,c=r+Vector[v][0],c+Vector[v][1]
        if r==c==2:
            break
    else:
        turn+=1
        continue
    break
    
print( sum( [Map[i][j] for i in range(N+4) for j in range(N+4) if i not in range(2,N+2) or j not in range(2,N+2)]))
