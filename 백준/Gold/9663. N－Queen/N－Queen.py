N=int(input())
#current[0]은 해당 열에 원소가 들어온 적이 있는지이다.
#만약 current[0]=[1]이라면 1번 열에 퀸이 들어온 적이 있으므로 이후의 행에 1은 못들어온다.
#current [1]은 합이 같은 친구들이다. 즉, 좌하단에서 우상단으로 가는 대각선이다.
#이 값이 같다는 것은 같은 대각선이란 뜻이다.
#current [2]는 차가 같은 친구들이다. 즉 좌상단에서 우하단으로 가는 대각선이다.
#체스판은 대칭이므로 0행에서 반까지의 경우의 수만 확인하고 *2를 하면 된다.(홀수일 경우는 +1)

def DFS(stack):#current는 i,i+stack,i-stack
    global score

    if stack==N:
        score+=1
        return 0
    
    for i in range(N):
        if M[i]*L[i+stack]*R[i-stack]:
            M[i]=0
            L[i+stack]=0
            R[i-stack]=0
            DFS(stack+1)
            M[i]=1
            L[i+stack]=1
            R[i-stack]=1
    




score=0
M=[1]*N
L=[1]*2*N
R=[1]*2*N
for i in range(N//2):
    M[i]=0
    L[i]=0
    R[i]=0
    DFS(1)
    M[i]=1
    L[i]=1
    R[i]=1
    
score*=2
if N%2:
    L[N//2]=0
    R[N//2]=0
    M[N//2]=0
    DFS(1)
print(score)
