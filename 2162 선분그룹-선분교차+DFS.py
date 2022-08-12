#테스트삼아 돌리는거 점인 경우?
N=int(input())
List=[]
visited=[0]*N
for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    List.append((x1,y1,x2,y2))

def check(A,B):
    x1,y1,x2,y2=A
    a1,b1,a2,b2=B
    dx=x2-x1
    dy=y2-y1
    da=a2-a1
    db=b2-b1
    c1=dx*y1-dy*x1
    c2=da*b1-db*a1

    dxa=x1-a1
    dyb=y1-b1
    #직선1: #테스트
    if dx==dy==0 or da==db==0:
        print(0)
    elif (dx)*(db)==(dy)*(da):#평행하면 안만남
        if dx*dyb==dy*dxa and ((min(a1,a2)<=min(x1,x2)<=max(a1,a2) and min(b1,b2)<=min(y1,y2)<=max(b1,b2))
                               or (min(x1,x2)<=min(a1,a2)<=max(x1,x2) and min(y1,y2)<=min(b1,b2)<=max(y1,y2))):
            return 1
        else:
            return 0

    else:
        X=(da*c1-dx*c2)/(dx*db-da*dy)
        Y=(db*c1-dy*c2)/(dx*db-da*dy)
        if (min(x1,x2)<=X<=max(x1,x2) and min(a1,a2)<=X<=max(a1,a2) and
            min(y1,y2)<=Y<=max(y1,y2) and min(b1,b2)<=Y<=max(b1,b2)):
            return 1
        else:
            return 0
        
G=0#the number of group
S=0#the biggest group size
for i in range(N):
    if visited[i]==0:
        que=[i]#i이후로만 확인하면 됨
        visited[i]=1
        cnt=1
        while que:
            A=List[que.pop()]
            for j in range(i+1,N):#나중에 추가된 선분이 앞에서 안만났던거랑 만날 수도 있으니 확인 
                B=List[j]
                if visited[j]==0 and check(A,B):
                    que.append(j)
                    visited[j]=1
                    cnt+=1
        S=max(S,cnt)
        G+=1
print(G)
print(S)

