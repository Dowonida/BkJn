import sys
input = sys.stdin.readline


#2000000 = 21번
N=1024*1024*2 #좌우 순서가 바뀌면 안됨
seg = [0]*2*N
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        idx = b+N
        while idx:
            seg[idx] +=1
            idx //=2
    else:
        idx = 1
        seg[idx] -= 1
        while idx<N:
 
            if seg[2*idx]<b:
                b -= seg[2*idx]
                idx = idx*2+1
            else:
                idx *= 2
            seg[idx]-=1
        print(idx-N)
