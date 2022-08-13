import sys
input=sys.stdin.readline

#홀짝 겹치면 NO하고 다 빠져나오기
#당연히 확인해야하는거 삼각형, 오각형
#주의해야하는거 사각형, 분리집합
T=int(input())

for test_case in range(T):
    N, M = map(int,input().split())
    dic = {i:set() for i in range(1,N+1)}
    for i in range(M):
        a,b=map(int,input().split())
        dic[a].add(b)
        dic[b].add(a)
    visited= {}
    
    for X in range(1,N+1):
        if X in visited:
            continue

        que=[X]
        
        turn=1

        while que:
            nq=set()
            for a in que:
                
                if a not in visited:
                    visited[a]=turn
                else:
                    if visited[a]!=turn:
                        print("NO")
                        break
                    else:
                        continue
                for i in dic[a]:
                    dic[i].remove(a)
                    if i not in visited:
                        nq.add(i)
            else:
                que=nq
                turn*=-1
                continue
            break
        else:
            continue
        break
    else:
        print("YES")


