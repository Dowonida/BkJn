import sys
sys.setrecursionlimit(250000)
input=sys.stdin.readline
R,C=map(int,input().split())
def tracking(r,c):
    global R,C
    if (r,c) in DP:
        return DP[(r,c)]
    base=Map[r][c]
    rst=0
    if r>0 and Map[r-1][c]>base:
        rst+=tracking(r-1,c)
    if r<R-1 and Map[r+1][c]>base:
        rst+=tracking(r+1,c)
    if c>0 and Map[r][c-1]>base:
        rst+=tracking(r,c-1)
    if c<C-1 and Map[r][c+1]>base:
        rst+=tracking(r,c+1)
    DP[(r,c)]=rst
    return DP[(r,c)]

Map=[]
DP={} #해당지점까지 가는 경로의 수
#끝지점에 가는 경로의 수 역추적할 예정 
for i in range(R):
    Map.append(list(map(int,input().split())))

DP[(0,0)]=1

print(tracking(R-1,C-1))
