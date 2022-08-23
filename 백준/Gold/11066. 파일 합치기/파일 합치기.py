T=int(input())
for test_case in range(T):
    N=int(input())
    DP=[ [0] * N for i in range(N)]
    M=list(map(int,input().split()))
    cnt=0
    for i in range(1,N):#행과 열의 차이가 i
        for j in range(i,N):
            DP[j-i][j]=sum(M[j-i:j+1])+min([ DP[j-i][j-k]+DP[j-i+i-k+1][j] for k in range(1,i+1)])
    print(DP[0][-1])
            
