N, M =map(int,input().split())
Vector=[0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
Map=[ [0]*(N+2)]
for i in range(N):
    Map.append([0]+list(map(int,input().split()))+[0])
Map.append([0]*(N+2))


que={ (N,1),(N,2),(N-1,1),(N-1,2)}
for i in range(M):
    nq=set()
    v, s = map(int,input().split())
    dr, dc = Vector[v]
    dr*=s
    dc*=s
    visited={ ((a+dr-1)%N+1,(b+dc-1)%N+1) for a,b in que}
    #print(visited)
    for r,c in visited:
        Map[r][c]+=1
    for r,c in visited:
        Map[r][c]+=len( [ _ for _, __ in ((r-1,c-1),(r-1,c+1),(r+1,c-1),(r+1,c+1))
                            if Map[_][__]])
    for r in range(1,N+1):
        for c in range(1,N+1):
            if (r,c) in visited:
                continue
            if Map[r][c]>=2:
                Map[r][c]-=2
                nq.add((r,c))
    que=nq
print ( sum( [sum(i) for i in Map]))        
        
    
