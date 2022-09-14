
A=input()
B=input()
N=len(B)

DP=[0]*N

for i in range(len(A)):
    cnt=0
    for j in range(len(B)):
        if cnt<DP[j]:
            cnt=DP[j]
        elif A[i]==B[j]:
            DP[j]=cnt+1

print(max(DP))
