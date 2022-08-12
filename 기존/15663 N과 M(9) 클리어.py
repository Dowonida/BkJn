import sys

def DFS(L,Current):
    if len(Current)==M:
        rst=''
        for i in Current:
            rst+=str(i)+' '
        RST[rst]=1
    for i in range(len(L)):
        A=L.copy()
        Current.append(A.pop(i))
        DFS(A,Current)
        Current.pop()


N,M=map(int,sys.stdin.readline().split())
List=list(map(int,sys.stdin.readline().split()))
List.sort()
RST={}
DFS(List,[])
for i in RST:
    print(i)