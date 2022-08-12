import sys

def DFS(n,T):
    global N, M
    if len(T)==M:
        rst=''
        for i in T:
            rst+=str(i)+' '
        RST.append(rst)
        return 0
    for i in range(n,N+1):
        T.append(i)
        DFS(i,T)
        T.pop()





N, M=map(int,sys.stdin.readline().split())
RST=[]
DFS(1,[])
for i in RST:
    print(i)