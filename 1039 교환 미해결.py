N,K=input().split()
N=list(N)
K=int(K)#바꿀횟수

check=0
for i in range(len(N)):
    if N[i] in N[i+1:]:
        check=1
        break
#후처리 리스트, 중복맥시멈에 대한 교환 결과 정렬 인덱스를 저장해서 튜플로 정렬
#이렇게 할 예정 hcr[[1,2,3]]일 경우 N[1],N[2],N[3]=tuple([N1,N2,N3]정렬,리버스)
if len(N)==1 and K>0:
    print(-1)
elif '0' in N and len(N)==2:
    print(-1)
else:
    zrs=0 #대상자리수
    cnt2=0 #중복숫자 처리
    hcr=[]
    while K>0 and N[zrs:]!=[]:#K가 0이 되면 더 못바꾸고, zrs가 len(N)보다 크면 다 바꿔서 후처리 필요
        Max=max(N[zrs:])
        NN=N.copy()
        NN.reverse()

        a=len(N)-1-NN.index(Max)
        if N[zrs]==Max:
            zrs+=1
        else:
            if N.count(Max)>1 and cnt2==0:
                cnt2=N.count(Max)

            N[zrs],N[a]=N[a],N[zrs]
            if cnt2>0:
                hcr.append(a)
                if cnt2==1:
                    HCR=[ N[j] for j in hcr]
                    HCR.sort(reverse=True)
                    hcr.sort()
                    for j in range(len(hcr)):
                        N[hcr[j]]=HCR[j]
                    hcr=[]
                cnt2-=1
            K-=1
            zrs+=1


    if hcr:
        HCR=[ N[j] for j in hcr]
        HCR.sort(reverse=True)
        hcr.sort()
        for j in range(len(hcr)):
            N[hcr[j]]=HCR[j]    
    if K%2==1 and check==0:
        N[-1],N[-2]=N[-2],N[-1]
    rst=''
    for i in N:
        rst+=i
    print(rst)

#반례목록
#교환 불가인 경우 0이 1개, 숫자가 1개인 경우
#교환불가같은데 가능인 경우 0이 2개이상
#앞에서부터 교환시 교환횟수 부족일경우 문제됨
#교환횟수 충분시 나머지들의 위치가 문제됨
#또반례
# #3251666같은 경우 현재 알고리즘으론 (제일큰거 당겨오기, 밀려난거 정렬)
# 6661532가 된다. 3번교환의 경우 이것이 최고지만
# 4번교환의 경우 여기서는 6665132가 된다.
# 3번교환에서 6661325로 바꿨었다면 4번교환에서 6665321이 된다. 
# 완전내림차순으로 만든 다음에 남은교환횟수에 대해서는 기치환 우치환을 생각해보면 걱정 없다.
# 즉 남은 교환횟수의 홀짝 여부가 바뀌진 않는다. 