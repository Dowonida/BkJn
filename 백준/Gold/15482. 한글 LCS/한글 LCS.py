A=input()
B=input()

LA=len(A)
LB=len(B)

DP=[0]*LB
m=0
for i in range(LA):
    cs=0
    for j in range(LB):
        if cs<DP[j]:
            cs=DP[j]
        elif A[i]==B[j]:
            DP[j]=cs+1
            m=max(m,cs+1)
        
print(m)
