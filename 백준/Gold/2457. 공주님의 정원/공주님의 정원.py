import sys
input=sys.stdin.readline

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
L.sort(key=lambda x: (x[0],x[1]))
start=(3,1)
end=(3,1)
idx=0
rst=0

while idx<N:
    if (L[idx][0],L[idx][1])>start:
        break
    while idx<N and (L[idx][0],L[idx][1])<=start:
        end=max(end,(L[idx][2],L[idx][3]))
        idx+=1
    rst+=1
    start=end
    if start>(11,30):
        break
if end<=(11,30):
    print(0)
else:
    print(rst)
