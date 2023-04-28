import sys
input = sys.stdin.readline

N= int(input())

NN = 1<<17



L = [[0,0] for _ in range(NN*2)]  #[합,단일최대]

A = list(map(int,input().split()))
for i in range(1,N+1):
    L[i+NN][1] = A[i-1]


for i in range(NN-1,0,-1):
    L[i][0] = max(L[i*2][0],L[i*2+1][0],L[i*2][1]+L[i*2+1][1])
    L[i][1] = max(L[i*2][1],L[i*2+1][1])


for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a==1:
        idx = b+NN
        L[idx][1] = c
        idx //= 2
        while idx:
            L[idx][0] = max(L[idx*2][0],L[idx*2+1][0],L[idx*2][1]+L[idx*2+1][1])
            L[idx][1] = max(L[idx*2][1],L[idx*2+1][1])
            idx //= 2

    else:
        sidx = b+NN
        eidx = c+NN+1
        rst = [0,0]
        while sidx<eidx:
            if sidx%2:
                rst= [max(rst[0],L[sidx][0],rst[1]+L[sidx][1]),
                      max(rst[1],L[sidx][1])]
                
                sidx += 1

            if eidx%2:
                eidx -= 1
                rst= [max(rst[0],L[eidx][0],rst[1]+L[eidx][1]),
                      max(rst[1],L[eidx][1])]   
            sidx //= 2
            eidx //= 2
        print(rst[0])
            
