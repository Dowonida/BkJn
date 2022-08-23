T = int(input())
#DP풀이
for test_case in range(1, T + 1):
    d,M,T,Y=map(int,input().split())
    M=min(M,T,Y)
    T=min(M*3,T,Y)
    Y=min(Y,4*T,12*M)
    DP=[0]+ [ min(i*d,M) for i in map(int,input().split())]#1달 이용권 최저값

    for i in range(1,13):
        Min=DP[i]+DP[i-1]
        if i>=3:
            Min=min(Min,DP[i-3]+T)
        if i==12:
            Min=min(Min,Y)
        DP[i]=Min
    print(f'#{test_case}',DP[-1])
    
