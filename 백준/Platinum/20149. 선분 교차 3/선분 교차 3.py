x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())
dx=x2-x1
dy=y2-y1
da=a2-a1
db=b2-b1
c1=dx*y1-dy*x1
c2=da*b1-db*a1

mx=min(x1,x2)
my=min(y1,y2)
ma=min(a1,a2)
mb=min(b1,b2)
Mx=max(x1,x2)
My=max(y1,y2)
Ma=max(a1,a2)
Mb=max(b1,b2)

mmr = min(x1,x2,a1,a2)
MMr = max(x1,x2,a1,a2)
mmc = min(y1,y2,b1,b2)
MMc = max(y1,y2,b1,b2)

dxa=x1-a1
dyb=y1-b1
#직선1: #테스트

if (dx)*(db)==(dy)*(da):#평행하면 안만남
    if dx*dyb==dy*dxa and ((ma<=x1<=Ma and mb<=y1<=Mb)
                           or (ma<=x2<=Ma and mb<=y2<=Mb)
                           or (mx<=a1<=Mx and my<=b1<=My)
                           or (mx<=a2<=Mx and my<=b2<=My)):
        if ((x1==a1 and y1==b1 and (x1 not in (mmr,MMr) or y1 not in (mmc,MMc)))
            or (x1==a2 and y1==b2 and (x1 not in (mmr,MMr) or y1 not in (mmc,MMc)))
            or (x2==a1 and y2==b1 and (x2 not in (mmr,MMr) or y2 not in (mmc,MMc)))
            or (x2==a2 and y2==b2 and (x2 not in (mmr,MMr) or y2 not in (mmc,MMc)))):
            print(1)
            print(*({(x1,y1),(x2,y2)}&{(a1,b1),(a2,b2)}).pop())
        else:
            print(1)
    else:
        print(0)

else:
    X=(da*c1-dx*c2)/(dx*db-da*dy)
    Y=(db*c1-dy*c2)/(dx*db-da*dy)
    if (mx<=X<=Mx and ma<=X<=Ma and
        my<=Y<=My and mb<=Y<=Mb):
        print(1)
        print(X,Y)

    else:
        print(0)
    
