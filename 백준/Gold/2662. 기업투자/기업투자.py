import sys
input = sys.stdin.readline

N, M = map(int,input().split())

Map = [ [0]*(N+1) for _ in range(M)] #행이 주식번호, 열은 해당인덱스만큼 투자

DP = [0]*(N+1)
order = ['' for _ in range(N+1)]

for i in range(N):
    a,*L = map(int,input().split())
    for j in range(M):
        Map[j][a] = L[j]

for i in range(M):
    NDP = [0]*(N+1)
    Norder=['0 ' for _ in range(N+1)]
    for j in range(N+1):
        for k in range(j+1):
            #나를 k번
            if Map[i][k]+DP[j-k]>NDP[j]:
                NDP[j] = Map[i][k]+DP[j-k]
                Norder[j] = order[j-k]+str(k)+' '
            
    DP = NDP
    order = Norder
    
print(DP[-1])
print(order[-1].strip())