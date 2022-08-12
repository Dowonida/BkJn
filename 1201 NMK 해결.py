N, M, K=map(int,input().split())
#M이 증가 K가 감소 
if M+K-1<=N<=K*M:
    List=['']*K*M
    cnt=-K

    for i in range(cnt,cnt+K):
        List[i]=str(N)+' '
        N-=1
    M-=1
    cnt-=K
    while M:
        Range=min(K,N-M)
        print(K,N-M)
        for i in range(cnt,Range+cnt):
            List[i]=str(N)+' '
            N-=1
        cnt-=K
        M-=1
    
    rst=''
    for i in List:
        rst+=i
    print(rst)
    

else:

    print(-1)
