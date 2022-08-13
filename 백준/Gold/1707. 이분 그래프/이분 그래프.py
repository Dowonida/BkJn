import sys
input=sys.stdin.readline
#sys.stdin=open('input.txt')

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


