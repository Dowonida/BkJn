N , K = input().split()
K=int(K)
M=len(N)
if ((len(N)==2 and N[1]=='0') or len(N)==1) and K:
    print(-1)
else:
    Max=''
    que={(N,K)}
    RST=[]
    while que:
        nq=set()
        for n,k in que:
            flag=False
            if k>0:
                for i in range(M-1):
                    for j in range(i+1,M):
                        if n[i]<n[j]:
                            nn=n[:i]+n[j]+n[i+1:j]+n[i]+n[j+1:]
                            nq.add((nn,k-1))
                            flag=True
            if not flag:
                if k%2:
                    for i in range(10):
                        if n.count(str(i))>1:
                            break
                    else:
                        n=n[:-2]+n[-1]+n[-2]
                Max=max(Max,''.join(n))
        que=nq
    print(Max)

