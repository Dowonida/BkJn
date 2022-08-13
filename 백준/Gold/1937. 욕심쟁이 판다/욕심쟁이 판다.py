import sys
input=sys.stdin.readline
sys.setrecursionlimit(250000)
#인접칸 중에서 가장 작은 친구들을 뽑아서 후보에 올림
#거기서부터 DFS로 길이 찾기

#인접칸 중에서 가장 큰 친구들을 뽑아서..?
#DP로 현재 최장길이를 저장함
#즉 (a,b)에 6번째로 온 기록이 있으면 3번째로 온 기록은 무시 
N=int(input())
Map=[]
for i in range(N):
    Map.append(list(map(int,input().split())))

start=set()# 시작점 큐가 됨 근처에서 가장 작은 친구들 
#기준점보다 큰 인접좌표를 저장 
DP=[[[] for j in range(N)] for i in range(N)]
LDP={}
for r in range(N):
    for c in range(N):
        cnt=1
        if r>0:
            if Map[r-1][c]>Map[r][c]:
                DP[r][c].append((r-1,c))
            else:
                cnt=0
        if r<N-1:
            if Map[r+1][c]>Map[r][c]:
                DP[r][c].append((r+1,c))
            else:
                cnt=0
        if c>0:
            if Map[r][c-1]>Map[r][c]:
                DP[r][c].append((r,c-1))
            else:
                cnt=0
        if c<N-1:
            if Map[r][c+1]>Map[r][c]:
                DP[r][c].append((r,c+1))
            else:
                cnt=0
        if cnt==1:
            start.add((r,c))

def DFS(x):
    r,c=x
    if (r,c) in LDP:
        return LDP[(r,c)]
    
    if not DP[r][c]:#가장 높아서 더 갈 곳이 없는 경우
        LDP[(r,c)]=1

        return 1
    rst=0
    for X in DP[r][c]:
        rst=max(rst,DFS(X))
    LDP[(r,c)]=rst+1
    return rst+1

rst=1
for i in start:
    rst=max(rst,DFS(i))
print(rst)
