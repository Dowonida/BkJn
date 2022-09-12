import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

#노선이 편도야 왕복이야?
#일단 편도라고 칠까?

dic={ i:{} for i in range(N+1)}
for i in range(M):
    a,b,c=map(int,input().split())
    if b not in dic[a]:
        dic[a][b]=c
    else:
        dic[a][b]=min(dic[a][b],c)

s, e = map(int,input().split())

visited=[0]*(N+1)
dist=[1e10]*(N+1)
prev=[-1]*(N+1)


visited[s]=1
dist[s]=0
for i in dic[s]:
    dist[i]=dic[s][i]
    prev[i]=s
    
for i in range(N-1):
    Nidx=-1
    Ndist=1e10
    for j in range(1,N+1):
        if visited[j]==0 and Ndist>=dist[j]:
            #연결이 끊어져 있을 수가 있다.
            #그런 경우 해당 노드는 마지막까지 남게되고
            #dist[j]는 초기값 1e10에서 갱신되지 않는다.(낮아지지 않는다.)
            #따라서 이런 경우에 Ndist>=dist[j]로 두면 해당 루트를 타고 내려오면서
            #인덱스가 갱신되지 않아서 -1로 남게 되고
            #그 결과 -1 키에러가 뜬다.
            Nidx=j
            Ndist=dist[j]

    visited[Nidx]=1
    for j in dic[Nidx]:
        if visited[j]==0 and dist[Nidx]+dic[Nidx][j]<dist[j]:
            prev[j]=Nidx
            dist[j]=dist[Nidx]+dic[Nidx][j]

print(dist[e])
prevs=[e]
while prevs[-1]!=s:
    prevs.append(prev[e])
    e=prev[e]
print(len(prevs))
print(*prevs[::-1])
