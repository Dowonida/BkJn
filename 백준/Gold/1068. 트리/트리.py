N=int(input())

Sons={i:[] for i in range(-1,N)}
L=list(map(int,input().split()))
D=int(input())
for i in range(N):
    if i!=D:
        Sons[L[i]].append(i)
    

#D의 부모노드의 Sons목록에서 D를 지워야함
rst=0
que=Sons[-1]#루트임
while que:
    a=que.pop()
    if Sons[a]:
        que+=Sons[a]
    else:
        rst+=1
print(rst)
        
