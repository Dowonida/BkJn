N=int(input())
#current[0]은 해당 열에 원소가 들어온 적이 있는지이다.
#만약 current[0]=[1]이라면 1번 열에 퀸이 들어온 적이 있으므로 이후의 행에 1은 못들어온다.
#current [1]은 합이 같은 친구들이다. 즉, 좌하단에서 우상단으로 가는 대각선이다.
#이 값이 같다는 것은 같은 대각선이란 뜻이다.
#current [2]는 차가 같은 친구들이다. 즉 좌상단에서 우하단으로 가는 대각선이다.
#체스판은 대칭이므로 0행에서 반까지의 경우의 수만 확인하고 *2를 하면 된다.(홀수일 경우는 +1)

def DFS(current,stack):#current는 i,i+stack,i-stack
    global score

    if stack==N:
        score+=1
        return 0
    
    for i in range(N):
        if i not in current[0] and i+stack not in current[1] and i-stack not in current[2]:
            current[0].append(i)
            current[1].append(i+stack)
            current[2].append(i-stack)
            DFS(current,stack+1)
            current[0].pop()
            current[1].pop()
            current[2].pop()
    




score=0
for i in range(N//2):
    DFS([[i],[i],[i]],1)
score*=2
if N%2:
    DFS([[N//2],[N//2],[N//2]],1)
print(score)
