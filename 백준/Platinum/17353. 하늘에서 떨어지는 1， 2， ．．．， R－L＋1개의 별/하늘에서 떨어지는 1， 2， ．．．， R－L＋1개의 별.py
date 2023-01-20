import sys
input = sys.stdin.readline

N = int(input())+1
seg = [[0,0,0] for _ in range(N+1)]+list(
    map(lambda x: [int(x),0,0],input().split())) #합,더한횟수,시작인덱스

for i in range(N+1,2*N):
    seg[i][2] = i-N
for i in range(N-1,0,-1):
    seg[i][2] = min(seg[i*2][2], seg[i*2+1][2])
#세그먼트에는 각각 '첫 인덱스에'더해진 별의 개수를 적는다.
#가령 [1,2]를 포함하는 노드에 별이 떨어졌다면
#해당 노드에는 1이 저장된다.
#그러면 첫번째에 해당하는 1에는 +1, 두번째인 2에는 +2를하면 된다.
#만약 [1,2], [3,4,5,6]에 떨어진다면
#[1,2]에는 1이 저장되고, [3,4,5,6]에는 3이 저장된다.
#이는 [3,4,5,6]의 첫인덱스부터 3,4,5,6개를 더해준다는 말이 된다.
#그런데 이럴 경우 [3,4,5,6]에 1이 저장된 다음 2가 추가된 경우랑
#처음부터 3이 저장된 경우를 구분하지 못한다.
#1이 저장된 다음 2가 추가된다면 각 인덱스에 3,5,7,9를 더해주어야하기 때문이다.
#따라서 추가된 횟수도 필요하다.

for _ in range(int(input())):
    A = map(int,input().split())
    if next(A) == 1:
        s, e = A
        s += N
        e += N+1
        scnt = 1#더해줄 개수
        ecnt = 1#더해줄 개수 (구간 길이)
        sidx = 1#구간의 첫번째 수의 번호 
        eidx = e-s+1#구간의 첫번째 수의 번호 
        while s<e:
            if s%2:
                seg[s][1] += 1 #처리된 횟수 + 1
                seg[s][0] += sidx
                sidx += scnt
                s += 1
            if e%2:
                e -= 1
                seg[e][1] += 1
                eidx -= ecnt
                seg[e][0] += eidx
                
            s //= 2
            e //= 2
            scnt *= 2
            ecnt *= 2
    else:
        rst = 0
        q, = A
        qidx = q+N
        while qidx:
            rst += seg[qidx][0]+seg[qidx][1]*(q-seg[qidx][2])
            qidx //= 2
        print(rst)
        
