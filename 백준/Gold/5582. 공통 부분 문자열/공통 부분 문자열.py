A=input()
B=input()

DP=[[0]*(len(A)+1) for i in range(len(B)+1)]
rst=0
for i in range(len(B)):
    for j in range(len(A)):
        if B[i]==A[j]:
            DP[i+1][j+1]=DP[i][j]+1
    rst=max(max(DP[i+1]),rst)

print(rst)
