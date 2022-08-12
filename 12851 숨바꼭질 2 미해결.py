N, K = map(int,input().split())

Map=[0]*100001
DP=[1]*100001
for i in range(N):
    Map[i]=N-i

for i in range(N+1,100001):
    if i%2==0:
        if Map[i-1]==Map[i//2]:
            Map[i]=Map[i-1]
            DP[i]=DP[i-1]+DP[i//2]
        elif Map[i-1]<Map[i//2]:
            Map[i]=Map[i-1]+1
            DP[i]=DP[i-1]
        else:
            Map[i]=Map[i//2]+1
            DP[i]=DP[i//2]
        if Map[i-1]==Map[i]+1:
            DP[i-1]+=DP[i]
        elif Map[i]<Map[i-1]:
            Map[i-1]=Map[i]+1
            DP[i-1]=DP[i]

    else:
        Map[i]=Map[i-1]+1
        DP[i]=DP[i-1]
print(Map[K])
print(DP[K])

#비슷하지만 다른 문제이다 x2에 이동횟수가 생기기도해서
#-2, -3한게 x2랑 속도가 같을 수도 있다.