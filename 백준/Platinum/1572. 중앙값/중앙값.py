import sys
input = sys.stdin.readline


N, K = map(int,input().split())
L = [int(input()) for _ in range(N)]
F = (K+1)//2

S = sorted(set(L))
dic = {}
for i in range(len(S)):
    dic[ S[i]] = i


NN = 1024*256

seg = [0]*2*NN
for i in range(K-1):
    seg[dic[L[i]]+NN]+=1


for i in range(NN-1,0,-1):
    seg[i] = seg[i*2]+seg[i*2+1]


rst  = 0
for i in range(K-1,N):
    idx = dic[L[i]]+NN
    while idx:
        seg[idx] += 1
        idx //= 2

    cnt = F
    idx = 1
    while idx<NN:
        if seg[idx*2]<cnt:
            cnt -= seg[idx*2]
            idx = idx*2+1
        else:
            idx *= 2
    rst += S[idx-NN]
    




    idx = dic[L[i-K+1]]+NN
    while idx:
        seg[idx] -= 1
        idx //= 2

print(rst)
