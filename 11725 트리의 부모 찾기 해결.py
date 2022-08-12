import sys
input=sys.stdin.readline
N=int(input())

Tree={i:[] for i in range(1,N+1)}
Parents={}
for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)


que=[1]
while que:
    nq=[]
    for i in que:
        for j in Tree[i]:
            nq.append(j)
            Tree[j].remove(i)
            Parents[j]=i
        #부모만 남기기
        
    que=nq

for i in range(2,N+1):
    print(Parents[i])

