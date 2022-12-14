import sys
input=sys.stdin.readline
N=int(input())
MapB=[]
cs1=[0,0,0]
cs2=[0,0,0]
for i in range(N):
    x,y,z=map(int,input().split())
    a,b,c=tuple(cs1)
    d,e,f=tuple(cs2)
    cs1[0]=min(a,b)+x
    cs1[1]=min(a,b,c)+y
    cs1[2]=min(b,c)+z
    cs2[0]=max(d,e)+x
    cs2[1]=max(d,e,f)+y
    cs2[2]=max(e,f)+z



print(max(cs2),min(cs1))