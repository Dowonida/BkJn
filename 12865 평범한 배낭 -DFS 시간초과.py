import sys
def DFS(w,v,index):
    global rst
    hubo=[i for i in range(index+1,N) if K>=w+dic[i][0] ]
    if hubo==[]:
        rst=max(rst,v)
    else:
        for i in hubo:
            DFS(w+dic[i][0],v+dic[i][1],i)
        

N,K=map(int,sys.stdin.readline().split())
dic={}
rst=0
for i in range(N):
    dic[i]=tuple(map(int,sys.stdin.readline().split()))

DFS(0,0,-1)
print(rst)
