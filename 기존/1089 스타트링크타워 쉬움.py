N=int(input())
Hub=[{0,1,2,3,4,5,6,7,8,9} for i in range(N)]
#그냥 불들어오면 후보목록에서 지우고 평균내면 끝
a=input()
b=input()
c=input()
d=input()
e=input()
for i in range(N):
    if b[4*i+1]=="#" or d[4*i+1]=="#":
        print(-1)
        break
    if d[4*i]=="#":
        Hub[i]-={1,3,4,5,7,9}
    elif e[4*i]=="#" or e[4*i+1]=="#":
        Hub[i]-={1,4,7}
    elif a[4*i+1]=="#":
        Hub[i]-={1,4}    
    if a[4*i]=="#":
        Hub[i]-={1}


    if b[4*i]=="#":
        Hub[i]-={1,2,3,7}
    elif d[4*i+2]=="#":
        Hub[i]-={2}


    if b[4*i+2]=="#":
        Hub[i]-={5,6}

    if c[4*i+1]=="#":
        Hub[i]-={0,1,7}
    elif c[4*i]=="#":
        Hub[i]-={1,7}

rst=0
Hub.reverse()
for i in range(N):
    rst+=(10**i)*(sum(Hub[i])/len(Hub[i]))
print(rst)
