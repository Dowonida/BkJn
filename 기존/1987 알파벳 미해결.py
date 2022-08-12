R,C = map(int, input().split())
Map=[[0]*(C+2)]
for i in range(R):
    Map.append([0]+list(input())+[0])

wall=[[1]*(C+2)]
for i in range(R):
    wall.append([1]+[0]*C+[1])
wall.append([1]*(C+2))
vector=[(-1,0),(1,0),(0,-1),(0,1)]
rst=0

def DFS(p,List):#p는 좌표 
    global rst
    if len(List)>rst:
        rst=len(List)
    x,y=p

    for dx,dy in vector:
        nx,ny=x+dx,y+dy
        if wall[nx][ny]==0 and Map[nx][ny] not in List:
            List.append(Map[nx][ny])
            DFS((nx,ny),List)
            List.pop()

            

DFS((1,1),[Map[1][1]])
print(rst)

'''
5 5
a b c d e
A B S C D
E a a a a
G H I J K
V W X Y Z
'''