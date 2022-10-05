N, K = map(int,input().split())

Map=[0]*100001
for i in range(N):
    Map[i]=N-i

for i in range(N+1,100001):
    if i%2==0:
        Map[i]=min(Map[i-1]+1,Map[i//2])
        if Map[i]<Map[i-1]:
            Map[i-1]=Map[i]+1
    else:
        Map[i]=Map[i-1]+1
print(Map[K])
