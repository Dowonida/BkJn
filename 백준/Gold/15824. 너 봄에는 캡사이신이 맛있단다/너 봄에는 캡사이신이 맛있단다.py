N = int(input())
mod = 1000000007

L=  sorted(map(int,input().split()))
M= [1]
for i in range(N):
    M.append((M[-1]*2)%mod)


rst = 0

for i in range(N):
    
    rst += M[i]*(L[i]-L[-1-i])
    rst %= mod

print(rst)
