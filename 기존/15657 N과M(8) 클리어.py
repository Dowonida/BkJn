import sys

def DFS(Num,Current):
    global N, M
    if len(Current)==M:
        rst=''
        for i in Current:
            rst+=str(i)+' '
        RST[rst]=1
        return 0
    if Num>=N:
        return 0
    for i in range(Num,N):
        Current.append(List[i])
        DFS(i+1,Current)
        Current.pop()
        
    
N,M= map(int,sys.stdin.readline().split())
List=list(map(int,sys.stdin.readline().split()))
List.sort()
RST={}
DFS(0,[])