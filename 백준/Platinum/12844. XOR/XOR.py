import sys
input = sys.stdin.readline

N = int(input())

'''
값을 출력하는 세그먼트 트리랑 = 초반 인풋 그대로
수정사항을 반영하는 세그먼트 트리를 운영할 예정

수정사항을 반영하는 세그먼트 트리는 구간의 길이와 무관하게
업데이트 된 값을 적어줌

조회할 때는 우선 초반 트리에서 값을 구한 다음에,
리프노드가 포함되면 올라가면서 처리


'''

seg1 = [0]*N+list(map(int,input().split()))
for i in range(N-1,0,-1):
    seg1[i] = seg1[i*2]^seg1[i*2+1]

seg2 = [0]*2*N

for _ in range(int(input())):
    a, *b = map(int,input().split())
    if a == 1:
        i,j,k = b
        s = i+N
        e = j+N+1

        
        while s<e:
            if s%2:
                if s>N:
                    ss = s
                    while ss:
                        seg1[ss] ^= k
                        ss //= 2
                else:
                    seg2[s] ^= k
                s += 1
            if e%2:
                e -= 1
                if e>N:
                    ee = e
                    while ee:
                        seg1[ee] ^= k
                        ee //= 2
                else:
                    seg2[e] ^= k
            s//=2
            e//=2
    else:
        i,j = b
        s = i+N
        e = j+N+1
        rst = 0
        if s%2:
            ss = s
            while ss:
                rst ^= seg2[ss]
                ss//=2
        if e%2:
            ee = e-1
            while ee:
                rst ^= seg2[ee]
                ee//=2
        while s<e:
            if s%2:
                rst ^= seg1[s]
                s += 1
            if e%2:
                e -= 1
                rst ^= seg1[e]
            s//=2
            e//=2
        print(rst)
