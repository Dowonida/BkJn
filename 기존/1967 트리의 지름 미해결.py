import sys
input=sys.stdin.readline

N=int(input())
Parent={i for i in range(1,N+1)}
Son={i for i in range(1,N+1)}
dic={}
for i in range(N):
    a,b,c=map(int,input().split())
    Parent.discard(b)
    Son.discard(a)
    dic[b]=c
    