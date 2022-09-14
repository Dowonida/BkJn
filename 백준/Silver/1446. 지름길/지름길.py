import sys
input=sys.stdin.readline

N, D = map(int,input().split())

dic={}
point=set()
for i in range(N):
    a,b,c= map(int,input().split())
    if b>D or c>b-a:#필요없는길 무시
        continue
    point.update((a,b))
    if b not in dic:
        dic[b]={a:c}
    else:
        if a not in dic[b]:
            dic[b][a]=c
        else:
            dic[b][a]=min(dic[b][a],c)

point.add(D)
point=sorted(list(point))
DP={i:i for i in point}

for i in range(1,len(point)):
    if point[i] not in dic:#딕셔너리 자체에 없는 경우 
        dic[point[i]]={point[i-1]:point[i]-point[i-1]}
        
    elif point[i-1] not in dic[point[i]]:#딕셔너리엔 있지만 이전 점이 없는경우
        dic[point[i]][point[i-1]]=point[i]-point[i-1]
    for j in dic[point[i]]:
        DP[point[i]]=min(DP[point[i]],DP[j]+dic[point[i]][j])
    
print(DP[D])
