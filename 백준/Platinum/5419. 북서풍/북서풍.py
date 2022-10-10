import sys
input=sys.stdin.readline

for _ in range(1,int(input())+1):
    N=int(input())
    L= [ list(map(int,input().split())) for i in range(N)]
    L.sort(key=lambda x: x[1])
    seg=[0]
    cnt=L[0][1]
    #내 y좌표가 0이면 0~0을 찾아야함
    #s=0, e=1이 되는거 
    idx=0

    for i in L:
        if i[1]==cnt:
            seg[-1]+=1
        else:
            cnt=i[1]
            seg.append(1)
            idx+=1
        i[1]=idx
    idx+=1 #세그먼트 길이
    seg=[0]*idx+seg
    for i in range(idx-1,0,-1):
        seg[i]=seg[i*2]+seg[i*2+1]

    L.sort(key=lambda x: (x[0],-x[1]))
    rst=0
    for x,y in L:
        #y가 이하인 친구들
        my_idx=idx+y
        while my_idx>0:
            seg[my_idx]-=1
            my_idx//=2
        s=idx
        e=y+1+idx
        while s<e:
            if s%2:
                
                rst+=seg[s]
                s+=1
            s//=2
            if e%2:
                e-=1
                rst+=seg[e]
            e//=2           
    print(rst)
