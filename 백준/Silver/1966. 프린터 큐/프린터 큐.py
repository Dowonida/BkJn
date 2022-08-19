from collections import deque

T=int(input())

for test_case in range(T):
    N, M = map(int,input().split())
    List=deque([(i, k) for i,k in enumerate(map(int,input().split()))])
    cnt=0
    rst=-1
    while rst!=M:
        List.rotate(-List.index(max(List,key=lambda x:x[1])))
        rst=List.popleft()[0]
        cnt+=1
    print(cnt)
        
    
