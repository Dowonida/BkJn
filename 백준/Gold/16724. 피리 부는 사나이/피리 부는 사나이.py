import sys
input=sys.stdin.readline
#어차피 밖으론 안나가고 계속 움직이므로
#싸이클이 언젠가는 생김
#00부터 돌아서 싸이클이 생기면
#지금까지 움직였던 경로를 전부 visited처리하고
#싸이클이 된 도착지점에 safezone을 둔다.
#싸이클이 아닌데 visited가 된경우는
#싸이클이 끝났는데 나중에 들어온 경우이므로
#그냥 visited처리만 한다.
#safe zone의 수를 출력한다.
#어차피 맵을 나가는 방향이 없으므로 1차원쓰기 편함 
R, C = map(int,input().split())
V={"D":C,"U":-C,"L":-1,"R":1}

visited=set()
Map=[]
rst=[]
for i in range(R):
    Map+=list(map(lambda x: V[x],input().strip()))

for i in range(R*C):
    if i not in visited:
        cp=i
        L={cp}
        while True:
            cp+=Map[cp]
            if cp not in visited:
                L.add(cp)
                
                visited.add(cp)
            elif cp in L:
                rst.append(cp)
                break
            else:
                break
print(len(rst))