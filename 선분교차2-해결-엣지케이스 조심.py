x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())
dx=x2-x1
dy=y2-y1
da=a2-a1
db=b2-b1
c1=dx*y1-dy*x1
c2=da*b1-db*a1

dxa=x1-a1
dyb=y1-b1
#평행한 경우를 특히 조심할것. 선분이 포함되거나 일부만 겹치거나 등을 잘 짜야함 

if (dx)*(db)==(dy)*(da):#평행하면 안만남
    if dx*dyb==dy*dxa and ((min(a1,a2)<=min(x1,x2)<=max(a1,a2) and min(b1,b2)<=min(y1,y2)<=max(b1,b2))
                           or (min(x1,x2)<=min(a1,a2)<=max(x1,x2) and min(y1,y2)<=min(b1,b2)<=max(y1,y2))):
        print(1)
    else:
        print(0)

else:
    X=(da*c1-dx*c2)/(dx*db-da*dy)
    Y=(db*c1-dy*c2)/(dx*db-da*dy)
    if (min(x1,x2)<=X<=max(x1,x2) and min(a1,a2)<=X<=max(a1,a2) and
        min(y1,y2)<=Y<=max(y1,y2) and min(b1,b2)<=Y<=max(b1,b2)):
        print(1)
    else:
        print(0)
    
