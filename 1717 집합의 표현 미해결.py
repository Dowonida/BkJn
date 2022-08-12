import sys
input=sys.stdin.readline
#시간이 2초이고 메모리가 128이므로 시간을 충분히 줘 보자

n,m=map(int,input().split())
L=[[i] for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    for j in L:
        if b in j:
            break
    for k in L:
        if c in k:
            break
    if a==0:
        pass

    if a==1:
        pass