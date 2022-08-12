import sys

def DFS(List,Current):
    global N, M
    if len(Current)==M:
        rst=''
        for i in Current:
            rst+=str(i)+' '
        print(rst)
        return 0
    for i in List:
        Current.append(i)
        A=List.copy()
        A.remove(i)
        DFS(A,Current)
        Current.pop()
        
    
N,M= map(int,sys.stdin.readline().split())
L=list(map(int,sys.stdin.readline().split()))
L.sort()

DFS(L,[])