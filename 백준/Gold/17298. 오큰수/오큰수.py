N=int(input())
L=list(map(int,input().split()))

stack=[]
answer=[0 for i in L]
idx=0
while idx<len(L):
    while stack and L[idx]>L[stack[-1]]:
        a=stack.pop()
        answer[a]=L[idx]

    stack.append(idx)
    idx+=1
    
while stack:
    a=stack.pop()
    answer[a]=-1
print(*answer)
