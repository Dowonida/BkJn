import sys
input=sys.stdin.readline

N ,M =map(int,input().split())

teri=[i for i in range(M+1)]
def get(a):
    if teri[a]==a:
        return a
    else:
        teri[a]=get(teri[a])
        return teri[a]
def union(a,b):
    global M
    if a==b:
        return
    x=get(a)
    y=get(b)
    if x!=y:
        teri[y]=x
        M-=1

que=[]
visited=[0]*(N*N)
for i in range(1,M+1):
    a,b= map(int,input().split())
    a-=1
    b-=1
    visited[a*N+b]=i
    que.append(a*N+b)

turn=0
while M>1:
    for i in que:
        t=visited[i]
        if i%N>0 and visited[i-1]!=0:
            union(t,visited[i-1])

        if i%N<N-1 and visited[i+1]!=0:
            union(t,visited[i+1])

        if i//N>0 and visited[i-N]!=0:
            union(t,visited[i-N])
        if i//N<N-1 and visited[i+N]!=0:
            union(t,visited[i+N])
    if M==1:
        break
        
    nq=[]
    

    for i in que:
        t=visited[i]
        if i%N>0:
            if visited[i-1]==0:
                visited[i-1]=t
                nq.append(i-1)

        if i%N<N-1:
            if visited[i+1]==0:
                visited[i+1]=t
                nq.append(i+1)

        if i//N>0:
            if visited[i-N]==0:
                visited[i-N]=t
                nq.append(i-N)
        if i//N<N-1:
            if visited[i+N]==0:
                visited[i+N]=t
                nq.append(i+N)
    turn+=1
    que=nq
print(turn)
