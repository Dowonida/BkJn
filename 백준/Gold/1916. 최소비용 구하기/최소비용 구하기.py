from heapq import heappop, heappush
import sys
input=sys.stdin.readline
#아마도 다익스트라....
#완전탐색은 굳이?이고,, bfs는 턴은 세어도 가중치는 무시됨
#아까 처음해보긴했는데 기억해서 해보자
#우선 간선 정보 저장하고
#거리배열 초기값은 매우 큰 값으로 초기화
#시작점의 거리는 0
#방문 여부도 저장
#방문여부는 pop했을 때 정해야함
#왜냐하면 직접 가기 전까지는 거리가 갱신될 수 있기 때문
#양방향인지 일방인지도 확인필요 ->불확실하지만, 설명으로 보건데 편도인듯
#버스노선이 중첩되는 곳이 있는지는 불확실하지만
#일단 없다고 가정하고 작성해보자.


#1회차 시도-시간초과-아마도 중복해서 더해지는 노드때문인거같은데..
#실행해본 결과 중복노선이 있음 
#그냥 DFS로 싹 구해볼까..?->순환생기면 망함
#플로이드 워셜? 0.5초에 10억번은 좀..
#최소 갱신트리는? 그건 전체를 최소비용으로 연결하는거지 특정 두 지점이 최소는 아님

#2회차 시도- 별 잡다한거 쓰지말고 그냥 visited 기준으로 후보지 뽑고
#DP기준으로 min뽑아서 다음 점으로 쓰는게 가장 낫다.
#이렇게 하니까 통과 된다.

N=int(input())
M=int(input())

dic={i:{} for i in range(1,N+1)}
for i in range(M):
    a,b,c=map(int,input().split())
    if b not in dic[a]:
        dic[a][b]=c # 출발-도착-가중치
    else:
        dic[a][b]=min(dic[a][b],c)



start, end = map(int,input().split())

DP=[1000000000]*(N+1)   #나올 수 있는 최대 가중치 저장, 인덱스의 편의를 위해 1칸 추가
                        #반드시 도착 가능하므로 INF처리는 안해도 될 듯

DP[start]=0
visited=[0]*(N+1)


#점을 뽑아와서 거리 갱신
#

while visited[end]==0:
    point=min([i for i in range(1,N+1) if visited[i]==0], key= lambda x:DP[x])
    dist=DP[point]
    visited[point]=1

    for i in dic[point]:
        if visited[i]==0:
            DP[i]=min(DP[i],dist+dic[point][i])


            
print(DP[end])
