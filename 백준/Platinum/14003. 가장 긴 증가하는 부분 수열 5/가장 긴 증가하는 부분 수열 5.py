import bisect
#역시 이진탐색을 잘못 구현해서 틀렸네... 다시 해봐야겠다
N=int(input())+1
L=[-1e10]+list(map(int,input().split()))


#비교는 인덱스로 
#마지막 보다 크면 마지막에 추가
#마지막 보다 작으면 자리 이진탐색으로 찾기

previdx=[-1]*N
RST=[(1e10,0)]*N
RST[0]=(L[0],0) #값,인덱스
last=0
for i in range(1,N):
    Nidx=bisect.bisect_left(RST,(L[i],i))
    if RST[Nidx-1][0]==L[i]:
        continue
    RST[Nidx]=(L[i],i)
    previdx[i]=RST[Nidx-1][1]
    #print(last,Nidx)
    last=max(last,Nidx)

#print(RST)
RR=[]
idx=RST[last][1]
while idx>0:

    RR.append(L[idx])
    idx=previdx[idx]
print(len(RR))
print(*RR[::-1])
