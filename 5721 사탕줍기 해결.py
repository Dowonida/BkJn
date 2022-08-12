import sys
input=sys.stdin.readline
#전략: 행의 값을 구함
#행의 값은 행별로 dp최대
#이후 행의 값들로 다시 dp최대

while True:
    M,N=map(int,input().split())
    if (M,N)==(0,0):
        break
    Map=[0]
    for i in range(M):
        L=[0]+list(map(int,input().split()))
        DP=[0]*(N+1)
        DP[1]==L[1]
        for j in range(2,N+1):
            DP[j]==max(DP[j-1],DP[j-2]+L[j])
        Map.append(DP[-1])
    
    DP=[0]*(M+1)
    DP[1]=Map[1]
    for i in range(2,M+1):
        DP[i]=max(DP[i-1],DP[i-2]+Map[i])
    print(Map[-1])
