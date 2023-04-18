import sys
input = sys.stdin.readline
import bisect

N, M = map(int,input().split())

seg = [ [] for _ in range(N)] + list(map(lambda x: [int(x)+1024*1024*1024],input().split()))


for i in range(N-1,0,-1):
    L = seg[i*2]
    R = seg[i*2+1]
    Le, Re = len(L), len(R)
    Ls = Rs = 0
    while Ls<Le and Rs<Re:
        if L[Ls]<R[Rs]:
            seg[i].append(L[Ls])
            Ls += 1
        else:
            seg[i].append(R[Rs])
            Rs += 1

    for j in range(Ls,Le):
        seg[i].append(L[j])
    for j in range(Rs,Re):
        seg[i].append(R[j])

for _ in range(M):
    a,b,c = map(int,input().split())
    s = a+N-1
    e = b+N

    idxs = []
    while s<e:
        if s%2:
            idxs.append(s)
            s += 1
        if e%2:
            e -= 1
            idxs.append(e)
        s //= 2
        e //= 2
    rst = 0
    target = 2*1024*1024*1024
    while target:
        cnt = rst + target
        s1 = sum( [bisect.bisect_left(seg[i],cnt) for i in idxs])
        s2 = sum( [bisect.bisect_right(seg[i],cnt) for i in idxs])
        target//=2
        if s1<c:
            rst = cnt
    print(rst-1024*1024*1024)
    
