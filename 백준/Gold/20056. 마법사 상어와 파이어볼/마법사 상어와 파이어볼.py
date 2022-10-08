import sys
input=sys.stdin.readline

N, M, K = map(int,input().split())
#N이 맵 크기
#M은 파이어볼 수
#K는 이동횟수
Map=[[[] for j in range(N+1)] for i in range(N+1)]
#r,c는 좌표
#m은 질량
#s는 속도
#d는 방향
Vector=[ (-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


RST=0
que=set()
for _ in range(M):
    r,c,m,s,d= map(int,input().split())
    Map[r][c].append((m,s,d))
    RST+=m
    que.add((r,c))

for k in range(K):
    #print(Map)
    nextMap=[[[] for j in range(N+1)] for i in range(N+1)]
    nq=set()
    for r,c in que:
        for m,s,d in Map[r][c]:
            dr,dc=Vector[d]
            nr,nc=r+dr*s,c+dc*s
            nr,nc=(nr-1)%N+1, (nc-1)%N+1
            nq.add((nr,nc))
            nextMap[nr][nc].append((m,s,d))
            
    for r,c in nq:
        if len(nextMap[r][c])>1:
            mm=sum([ _[0] for _ in nextMap[r][c] ] )
            RST-= mm-4*(mm//5)
            if mm//5==0:
                nextMap[r][c]=[]
                continue
            
            mm//=5
            ss=sum( [_[1] for _ in nextMap[r][c] ])//len(nextMap[r][c])
            vs={ _[2]%2 for _ in nextMap[r][c]}
            if len(vs)==1:
                nextMap[r][c]=[ [mm,ss,dd] for dd in [0,2,4,6]]
            else:
                nextMap[r][c]=[ [mm,ss,dd] for dd in [1,3,5,7]]
    Map=nextMap
    que=nq

print(RST)
            
    
