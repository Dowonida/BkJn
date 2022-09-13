import sys
sys.setrecursionlimit(200000)

answer=[]
def pre(postL,postR,inoL,inoR):
    if inoL==inoR:
        return
    root=post[postR-1]
    
    answer.append(root)
    idx=Idx[root]-inoL
#    idx=ino[inoL:inoR].index(root)

    #ino에서 인덱스를 알아야함
    pre(postL,postL+idx,inoL,inoL+idx)
    pre(postL+idx,postR-1,inoL+idx+1,inoR)
    
N=int(input())
ino= list(map(int,input().split()))
post= list(map(int,input().split()))
Idx={}
for i in range(N):
    Idx[ino[i]]=i

pre(0,N,0,N)
print(*answer)


