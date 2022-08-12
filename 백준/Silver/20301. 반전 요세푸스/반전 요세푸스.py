N, K, M = map(int,input().split())


dic={i:[i-1,i+1] for i in range(1,N+1)}
dic[1][0]=N
dic[N][1]=1

def kill(man,K):
    for i in range(K):
        man=dic[man][1]

    p,n=dic[man]
    dic[p][1]=n
    dic[n][0]=p

    return man

def kill2(man,K):
    for i in range(K):
        man=dic[man][0]

    p,n=dic[man]
    dic[p][1]=n
    dic[n][0]=p

    return man

D=N

for i in range(N):
    if (i//M)%2==0:
        D=kill(D,K)
        print(D)
    else:
        D=kill2(D,K)
        print(D)
