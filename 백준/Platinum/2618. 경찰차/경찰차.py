import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
Pos = [ (1,1), (N,N)]+[ tuple(map(int,input().split())) for _ in range(K)]
#마지막 인덱스는 N+1
#따라서 범위는 N+2

def dist(a,b):
    return abs(Pos[a][0]-Pos[b][0]) + abs(Pos[a][1]-Pos[b][1])

Max = 100
DP = [ [0 for i in range(_)] for _ in range(K+2)]
DP[1][0] = (0,2,-1) #자동차가 각각 1,0에 있다는 뜻
                    #이동 거리가 0이고, 최근에 움직인게 2임
                    #첫 최근이동이 2번인 이유는 방향을 유지하기 위함
reverse = [0,2,1]
for i in range(2,K+2):
    for j in range(i-1):
        DP[i][j] = (DP[i-1][j][0]+dist(i,i-1), DP[i-1][j][1],j)

    idx = min( range(i-1), key = lambda x: DP[i-1][x][0]+dist(x,i))

    DP[i][i-1] = (DP[i-1][idx][0]+dist(idx,i), reverse[DP[i-1][idx][1]],idx) 
        
        
idx = min(range(K+1), key = lambda x: DP[-1][x])
print(DP[-1][idx][0])
rst = []
for i in range(K+1,1,-1):
    me = DP[i][idx]
    rst.append(me[1])



    idx = me[2]

RST=''
for i in range(1,1+K):
    #print(rst[-i])
    RST+=str(rst[-i])+'\n'
print(RST)