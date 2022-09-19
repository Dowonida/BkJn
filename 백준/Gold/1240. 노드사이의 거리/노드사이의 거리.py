import sys
input=sys.stdin.readline
N, M =map(int,input().split())

dic={i:{} for i in range(1,N+1)}
for i in range(N-1):
    a,b,c=map(int,input().split())
    dic[a][b]=c
    dic[b][a]=c
#(노드번호, 1번노드로부터의거리, 부모노드,깊이)를 저장
RST={1:(0,-1,0)}
stack=[(1,0,-1,0)]
while stack:
    node, dist, parent, depth = stack.pop()
    for i in dic[node]:
        if i in RST:
            continue
        stack.append( (i,dist+dic[node][i],node,depth+1))
        RST[i]=(dist+dic[node][i],node,depth+1)

for i in range(M):
    A,B=map(int,input().split())
    a=A
    b=B
    #깊이를 맞추는 과정
    while RST[a][2]>RST[b][2]:
        a=RST[a][1]
    while RST[b][2]>RST[a][2]:
        b=RST[b][1]
    #깊이 맞춰짐
    #공통부모를 찾는 과정
    while a!=b:
        a=RST[a][1]
        b=RST[b][1]
    #공통부모 찾음
    #두 노드 사이의 거리는 두 노드의 루트로부터의 거리 -2*공통부모의 루트로부터의 거리
    print(RST[A][0]+RST[B][0]-2*RST[a][0])
