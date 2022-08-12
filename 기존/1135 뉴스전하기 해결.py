from re import A


N=int(input())
NOD=list(map(int,input().split()))

if N==1:
    print(0)
else:
    NOD2=NOD.copy()
    NOD2.reverse()

    DP=[[] for i in range(N)]
    for i in range(len(NOD2)-1):
        if DP[-1-i]==[]:
            DP[NOD2[i]].append(0)
            continue
        DP[-1-i].sort()
        M=max(DP[-1-i][j]+len(DP[-1-i])-j for j in range(len(DP[-1-i])))


        DP[NOD2[i]].append(M)
    DP[0].sort()
    M=max(DP[0][j]+len(DP[0])-j for j in range(len(DP[0])))
    print(M)