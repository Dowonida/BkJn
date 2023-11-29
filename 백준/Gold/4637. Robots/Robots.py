import sys

while True:
    a,b = map(int,input().split())
    if a==-1:
        break

    rst = 0
    cnt = 1 #점의 개수 
    Map = [ [] for _ in range(25)]
    Map[a].append(b)
    while True:
        a,b = map(int,input().split())
        if a==0:
            break
        cnt += 1
        Map[a].append(b)
    for m in Map:
        m.sort()

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
                    
