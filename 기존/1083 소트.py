N=int(input())
L=list(map(int,input().split()))
S=int(input())

rst=[]
cnt=0#변경횟수
while len(rst)<N and S>0:
    M=max(L[:S+1])
    O=L.index(M)
    rst.append(M)
    L.remove(M)
    S-=O
