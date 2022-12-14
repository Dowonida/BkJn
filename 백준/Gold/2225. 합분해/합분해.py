def comb(a,b):
    bm=1
    bz=1
    b=min(b,a-b)
    for i in range(b):
        bm*=i+1
        bz*=a-i
    return bz//bm
N,K=map(int,input().split())

print(comb(N+K-1,N)%1000000000)
