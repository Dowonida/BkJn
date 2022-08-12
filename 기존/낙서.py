N=int(input())

#값, 방문한 사람 목록

Map=[]
for i in range(N):
    Map.append(list(map(int,list(input().strip()))))
    
    #R이 C에게 팔 때 가격

Max=0

que=[(0,0,1)]#사람번호, 가격, 깊이 
List=[]#방문한 사람 목록

while que:
    man, price, depth = que.pop()
    Max=max(Max,depth)
    if Max==N:
        break
    while len(List)>depth-1:
        List.pop()
    List += [man]
    for j in range(N):
        if j not in List and Map[man][j]>=price:
            que.append((j,Map[man][j],depth+1))
print(Max)