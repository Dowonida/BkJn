import sys
input=sys.stdin.readline

N=int(input())
L=[int(input()) for i in range(N)]
M=max(L)
DP=[0]*(1+M)

for i in L:
    for j in range(1,M+1):
        if DP[j]:
            x,y=i,j
            while x:
                x,y=y%x,x
            #y가 gcd
            DP[y]=(DP[y]+DP[j])%10000003
    DP[i]+=1

print(DP[1])
