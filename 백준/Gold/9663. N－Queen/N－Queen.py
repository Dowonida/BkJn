N=int(input())




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
DFS([[],[],[]],0)
print(score)