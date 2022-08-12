import sys

def DFS(Num,Current):
    global N, M
    if len(Current)==M:
        rst=''
        for i in Current:
            rst+=str(i)+' '
        dic[rst]=1
        return 0
    for i in range(Num,N):
        Current.append(L[i])
        DFS(i,Current)
        Current.pop()

N,M=map(int,sys.stdin.readline().split())
L=list(map(int,sys.stdin.readline().split()))
L.sort()
dic={}
DFS(0,[])
for i in dic:
    print(i)