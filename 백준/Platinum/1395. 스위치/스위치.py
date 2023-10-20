import sys
input = sys.stdin.readline

'''
각 노드에
버튼 on/off여부랑 켜진 개수를 적으면?


업데이트: 값은 무조건 N-cur로 변경
on/off여부는 무조건 1-cur로 뒤집기
개수는 위로 전


'''

N, M = map(int,input().split())

seg = [[0,1] for _ in range(2*N)] #개수, on/off

for _ in range(M):
    q, s, e = map(int,input().split())

    size = 1
    s += N-1
    e += N
    target_node = []
    while s<e:
        if s%2:
            target_node.append((s,size))
            s += 1
        if e%2:
            e -= 1
            target_node.append((e,size))
        s//=2
        e//=2
        size*=2

    if q == 0:
        for idx, size in target_node:
            before = seg[idx][0]
            after  = size-before
            diff = after-before
            seg[idx][1] *= -1
            while idx:
                
                seg[idx][0] += diff
                idx //= 2
                diff *= seg[idx][1]

    else:
        rst = 0
        for idx, size in target_node:
            switch = 1
            count = seg[idx][0]
            while idx:
                idx//=2
                switch *= seg[idx][1]
            if switch == 1:
                rst += count
            else:
                rst += size-count
        print(rst)
            
        
    
