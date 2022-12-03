N = int(input())
L = list(map(int,input().split()))
# 1,2,3,1,1 인 경우
# 3,3,1,1개로 묶는 것이 아닌
# 3,2,3으로 묶어야함 즉 19원이 답
# 2동이 3동보다 크면 최대한 높이 비슷하게 해주기 
sidx=0
eidx=2
rst = 0
while eidx<N:
    flat = min(L[sidx],max(0, L[sidx+1]-L[sidx+2]))
    L[sidx] -= flat
    L[sidx+1] -= flat
    rst += 5*flat
    if L[sidx]:
        a = L[sidx]
        b = min(L[sidx],L[sidx+1])
        c = min(b,L[sidx+2])
        rst += L[sidx]*3+ b*2 +c*2

        L[sidx] -= a
        L[sidx+1] -= b
        
        L[sidx+2] -= c
    sidx += 1
    eidx += 1

a,b = sorted(L[sidx:])
rst += max(a,b)*3 + min(a,b)*2
print(rst)
