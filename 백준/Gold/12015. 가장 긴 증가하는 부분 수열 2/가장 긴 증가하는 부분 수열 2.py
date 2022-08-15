N=int(input())

L=list(map(int,input().split()))

DP=[-1,L[0]]

for i in range(1,N):
    if L[i]>DP[-1]:
        DP.append(L[i])
    else:
        #자기 '이상'인 가장 첫 원소
        target=L[i]
        Ri=len(DP)-1
        Le=1
        D=(Ri+Le)//2
        while True:
            if DP[D]>=L[i] and DP[D-1]<L[i]:
                DP[D]=L[i]
                break
            if DP[D]<L[i]:
                Le=D+1
            else:
                Ri=D
            D=(Ri+Le)//2


print(len(DP)-1)
