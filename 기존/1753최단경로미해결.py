import sys

V,E=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline().split())
path={}
for i in range(E):
    S,E,L=(map(int,sys.stdin.readline().split()))
    if S not in path:
        path[S]={E:L}
    else:
        path[S][E]=L
    if E not in path:
        path[E]={S:L}
    else:
        path[E][S]=L

