#######BFS로 짜보자
import sys
input=sys.stdin.readline
#sys.stdin=open('input.txt')


T=int(input())
for test_case in range(T):
    N, M, W = map(int,input().split())
    #노드, 통로, 웜홀
    V=0
    start=set()
    dic= {i:{} for i in range(1,N+1)}
    for i in range(M):
        a,b,c=map(int,input().split())
        if a in dic[b]:
            dic[b][a]=min(dic[b][a],c)
            dic[a][b]=min(dic[a][b],c)
        else:
            V+=1
            dic[a][b]=c
            dic[b][a]=c
    for i in range(W):
        a,b,c=map(int,input().split())
        start.add(a)#웜홀 시작점이 강력후보니까
        c=-c
        if b not in dic[a]:
            V+=1
            dic[a][b]=c
        else:
            dic[a][b]=min(dic[a][b],c)
            
    flag=True
    for i in start:
        if flag==False:
            break
        visited={j: [10000000,0] for j in range(1,N+1)}#거리와 카운트
        que={i:0}#큐에 중복루트가 많아질 수 있으니 주의
        while que:
            nq={}
            for j in que:
                for k in dic[j]:
                    #거리는 que[j]+dic[j][k]
                    d= que[j]+dic[j][k]#que[j]가 지금까지 거리
                                        #dic[j][k]가 이동할 거리
                    
                    if d<visited[k][0]:#누적거리가 기존보다 짧으면
                        visited[k][0]=d#누적거리를 줄여줌
                        visited[k][1]+=1#방문횟수를 늘림
                        nq[k]=d#k를 큐에 추가함 
                        if visited[k][1]>V:#임시로 잡음
                            
                            flag=False 
                            break #k탈출
                        
                if flag==False:#j탈출 que
                    break
            if flag==False:#while 탈출
                break
            que=nq

    if flag==False:
        print("YES")
    else:
        print("NO")
            

        #벨만포드 N번갱신?

                
