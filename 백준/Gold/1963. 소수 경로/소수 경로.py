prime=set()
check=[0]*10000
for i in range(2,10000):
    if check[i]==0:
        if i>1000:
            prime.add(i)
        for j in range(i,10000,i):
            check[j]=1
N=int(input())
for _ in range(N):
    s, e = map(int,input().split())

    que=[s]
    visited=[-1]*10000
    visited[s]=0
    turn=0
    while que:
        turn+=1
        nq=[]
        for i in que:
            i1=i%1000
            i2=i//1000*1000+i%100
            i3=i//100*100+i%10
            i4=i//10*10
            for j in range(10):
                JJ=[i1+1000*j,i2+100*j,i3+10*j,i4+j]
                for k in JJ:
                    if k in prime and visited[k]==-1:
                        visited[k]=turn
                        nq.append(k)
        que=nq

    if visited[e]==-1:
        print("Impossible")
    else:
        print(visited[e])
