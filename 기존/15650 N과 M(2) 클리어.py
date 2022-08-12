import sys
def DFS(L,T):
    global stack, rst, N, M
    if len(L)==0:
        return 0
    for i in L:
        A=range(i+1,N+1)
        T+=str(i)+' '
        if len(T)//2==M:
            RST.append(T)

        else:
            DFS(A,T)
        T=T[:-2]
    
    
N,M=map(int,sys.stdin.readline().split())
rst=''
RST=[]

Lst=list(range(1,N+1))
DFS(Lst,'')
print(RST)
