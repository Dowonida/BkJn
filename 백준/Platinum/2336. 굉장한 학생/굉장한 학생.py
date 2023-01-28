import sys
input = sys.stdin.readline

N = int(input())
idxs = [0]*(N+1)
elses = [[0,0] for _ in range(N+1)]

for i, n in enumerate(map(int,input().split()),1):
    idxs[n] = i
for i, n in enumerate(map(int,input().split()),1):
    elses[ idxs[n] ][0] = i
for i, n in enumerate(map(int,input().split()),1):
    elses[ idxs[n] ][1] = i

NN = 1024*512
seg = [NN]*(NN*2)
elses[0] = [NN,NN]
#B값은 노드 번호, C 값은 값

rst = 0 
for b,c in elses:#idxs:
    #b, c = B[idx], C[idx]

    s = NN
    e = b+NN
    cnt = NN
    while s<e:

        if s%2:
            cnt = min(cnt,seg[s])
            s += 1
        if e%2:
            e -= 1
            cnt = min(cnt,seg[e])
        s //= 2
        e //= 2

    if c<cnt:
        rst += 1
        cnt = NN+b
        while cnt:
            seg[cnt] = min(seg[cnt],c)

            cnt //= 2
            

print(rst)
