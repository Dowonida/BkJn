N=int(input())
before=list(map(int,list(input())))
after=list(map(int,list(input())))
switching=[]
for i in range(N):
    switching.append((before[i]-after[i])%2)
#switching에서 0번이 0이면 앞의 2개 합해서 0
#즉 1,1이거나 0,0
if N==1:
    print(sum(switching))
else:
    L1=[1,(switching[0]-1)%2]#1로시작
    L2=[0,(switching[0])%2]#2로시작
    for i in range(2,N):
        L1.append((switching[i-1]+L1[i-2]+L1[i-1])%2)
        L2.append((switching[i-1]+L2[i-2]+L2[i-1])%2)
        pass
    #여기까지 실행했으면 마지막스위치빼곤 다 제대로 됨
    RST=[]
    if (L1[-1]+L1[-2])%2==switching[-1]:#L1 마지막 전구가 일치한다는 뜻
        RST.append(L1)
    if (L2[-1]+L2[-2])%2==switching[-1]:#두번째케이스에서 일치한다는 뜻
        RST.append(L2)

    
    if RST:
        print(min([sum(i) for i in RST]))
    else:
        print(-1)
