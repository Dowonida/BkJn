#매 싸이클마다 처음 cnt는 0 
#같으면 cnt+1의 값을 저장
#다르면 cnt는 max로 저장
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
DP=[0]*N

for i in range(N):
    cnt=0
    for j in range(N):
        if A[i]==B[j]:
            DP[j]=cnt+1
        elif A[i]>B[j]:
            cnt=max(cnt,DP[j])

print(max(DP))
