N = int(input())
K = int(input())
L = sorted(list(map(int,input().split())))
# 10000 n log n = 14만
L2 = [ L[i]-L[i-1] for i in range(1,N)]

print(sum(sorted(L2)[:N-K]))
