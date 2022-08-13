import sys
input=sys.stdin.readline

R,C=map(int,input().split())
Map=[]
Map.append([0]*(C+2))
for i in range(R):
    Map.append([0]+list(map(int,input().split()))+[0])

DP=[[0]*(C+2) for i in range(R+2)]#인접 얼음 개수 
survived=set()
for r in range(R):
    for c in range(C):
        if Map[r][c]:
            survived.add((r,c))
            DP[r][c]+=not Map[r-1][c]
            DP[r][c]+=not Map[r+1][c]
            DP[r][c]+=not Map[r][c+1]
            DP[r][c]+=not Map[r][c-1]


def BFS():
    if not survived:
        return 0
    r,c=survived.pop()
    survived.add((r,c))
    que=[(r,c)]
    visited={(r,c)}
    while que:
        nq=set()
        for r,c in que:
            if  Map[r-1][c]>0 and ((r-1,c) not in visited):
                nq.add((r-1,c))
                visited.add((r-1,c))
            if Map[r+1][c]>0 and ((r+1,c) not in visited):
                nq.add((r+1,c))
                visited.add((r+1,c))
            if Map[r][c+1]>0 and ((r,c+1) not in visited):
                nq.add((r,c+1))
                visited.add((r,c+1))
            if Map[r][c-1]>0 and ((r,c-1) not in visited):
                nq.add((r,c-1))
                visited.add((r,c-1))
        que=nq
    if len(visited)==len(survived):
        return 1
    else:
        return 2
year=0
Ter=BFS()
while True:
    if Ter==0:
        print(0)
        break
    elif Ter==2:
        print(year)
        break
    death=set()#새로 녹은 빙하는 나중에 처리해야해!
    for r,c in survived:
        Map[r][c]-=DP[r][c]
        if Map[r][c]<1:
            death.add((r,c))
    survived=set(survived)-death
    for r,c in death:
        DP[r-1][c]+=1
        DP[r+1][c]+=1
        DP[r][c-1]+=1
        DP[r][c+1]+=1
    if death:
        Ter=BFS()
    year+=1
