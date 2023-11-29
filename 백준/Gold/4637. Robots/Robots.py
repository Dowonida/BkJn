import sys

while True:
    a,b = map(int,input().split())
    if a==-1:
        break

    rst = 0
    Map = [ set() for _ in range(25)]
    Map[a].add(b)
    if a == 0:
        Map[25]
        continue
    while True:
        a,b = map(int,input().split())
        if a==0:
            break
        
        Map[a].add(b)
    for i in range(25):
        Map[i] = sorted(Map[i])
    cnt = 0
    for i in range(25):
        cnt += len(Map[i])

    while cnt:
        rst += 1
        col = 0
        for i in range(25):
            if Map[i] and Map[i][-1]>=col:
                last = Map[i].pop()
                cnt -= 1
                while Map[i] and Map[i][-1]>=col:
                    Map[i].pop()
                    cnt -= 1
                col = last
    print(rst)
                    
