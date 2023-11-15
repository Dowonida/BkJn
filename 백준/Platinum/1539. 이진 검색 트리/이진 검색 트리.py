import sys
input = sys.stdin.readline



N = int(input())


maxseg = [-1]*2*N
minseg = [N]*2*N
rst = 0

depth = [0]*(N+1)

for _ in range(N):
    num = int(input())
    s = N
    e = N+num
    low = -1
    while s<e:
        if s%2:
            low = max(low,maxseg[s])
            s += 1
        if e%2:
            e -= 1
            low = max(low,maxseg[e])
        s//=2
        e//=2
    s = N+num+1
    e = 2*N
    high = N
    while s<e:
        if s%2:
            high = min(high,minseg[s])
            s += 1
        if e%2:
            e -= 1
            high = min(high,minseg[e])
        s//=2
        e//=2
    depth[num] = max(depth[low],depth[high])+1
    rst += depth[num]

    idx = N+num
    while idx:
        maxseg[idx] = max(maxseg[idx],num)
        minseg[idx] = min(minseg[idx],num)
        idx//=2
print(rst)
        
