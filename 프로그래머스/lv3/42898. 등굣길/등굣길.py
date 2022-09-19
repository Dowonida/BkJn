def solution(m, n, puddles):
    answer = 0
    #가로먼저-> 세로 
    #
    DP=[[0]*(n+1) for i in range(m+1)]
    DP[1][1]=1
    for i in range(1,m+1): #i가 가로 [가로][세로]
        for j in range(1,n+1):
            if [i,j] in puddles:
                continue
            DP[i][j]=(DP[i][j]+DP[i-1][j]+DP[i][j-1])%1000000007
    
    return DP[-1][-1]