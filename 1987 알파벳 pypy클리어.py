R,C = map(int,input().split())
Map=[[0]*(C+2)]
for i in range(R):
    Map.append([0]+list(input())+[0])
Map.append([0]*(C+2))
vector=((-1,0),(1,0),(0,-1),(0,1))
que=[(1,1)]
visited=[]
rst=1
while que:
    r,c=que.pop()
    visited.append(Map[r][c])
    cnt=0
    for dr,dc in vector:
        if Map[r+dr][c+dc]!=0 and Map[r+dr][c+dc] not in visited:
            que.append((r+dr,c+dc))
            cnt+=1

    if cnt==0:
        visited.pop()
    print(visited,que)


"""
2 4
CAAB
ADCB
"""
