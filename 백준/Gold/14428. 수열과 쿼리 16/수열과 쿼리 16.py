import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int,input().split()))
seg = [0]*(2*N)

for i in range(N):
    seg[i+N] = (L[i],i+1)

for i in range(N-1,0,-1):
    seg[i] = min(seg[i*2],seg[i*2+1])





for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a==1:
        idx = b+N-1
        seg[idx] = (c,b)
        idx//=2
        while idx:
            seg[idx] = min(seg[idx*2],seg[idx*2+1])
            idx//=2
    else:
        rst = (10000000000,0)
        sidx = b+N-1
        eidx = c+N
        while sidx<eidx:
            if sidx%2:
                rst = min(seg[sidx],rst)
                sidx +=1
            if eidx%2:
                eidx -= 1
                rst = min(seg[eidx],rst)
            sidx//=2
            eidx//=2
        print(rst[1])

            
