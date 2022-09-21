N , K = input().split()
K=int(K)
M=len(N)
if ((len(N)==2 and N[1]=='0') or len(N)==1) and K:#교환못하면 ㅂㅇㅂㅇ
    print(-1)
else:
    Max=''
    que={(N,K)}
    RST=[]
    visited={(N,K%2)}
    while que:
        nq=set()
        for n,k in que: #커지게 
            flag=False
            if k>0:
                for i in range(M-1):
                    for j in range(i+1,M):
                        if n[i]<n[j]:
                            nn=n[:i]+n[j]+n[i+1:j]+n[i]+n[j+1:]
                            if (nn,(k-1)%2) not in visited:
                                visited.add((nn,(k-1)%2))
                                nq.add((nn,k-1))
                                flag=True
            if not flag:#더 바꿀게 없으면 후보
                if k%2:#남은 교환횟수 털기 
                    for i in range(10):#같은거 2개 있으면 둘이 교환
                        if n.count(str(i))>1:
                            break
                    else:#아니면 가장 적게 손해보기=끝에서 2개 교환
                        n=n[:-2]+n[-1]+n[-2]
                Max=max(Max,''.join(n))#교환 다 소진했으면 Max 새로고침
        que=nq
    print(Max)

