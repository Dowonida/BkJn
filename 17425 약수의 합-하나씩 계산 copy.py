import sys
#메모리가 충분해보이므로 테스트케이스에서 가장 큰값을 기준으로
#전부 구한 다음 불러오기
T=int(sys.stdin.readline())
for test_case in range(T):
    L=int(sys.stdin.readline())


    for i in range(2,L+1):
        rst=0
        if i not in F:#새로운 소수가 추가될때마다 모든 합성수의 값을 채울거임
            F={k:1 for k in range(1,L+1)}
            for j in [k for k in F if F[k]==1]:
                k=1#지수
                prod=1+i #현재 계수
                #계수란 기존수에 곱해진 값을 말한다.
                #예를 들어 i가 2인경우 key값에 2,4,8...을 곱하게되면
                #value에는 1+2, 1+2+4....가 곱해지게 되는데 이 1+2를 계수라고 하자.
                #현재 계수는 이전 계수+i^현재지수가 된다.
                while j*(i**k)<=L:
                    F[j*(i**k)]=0
                    rst+=
                    F[j*(i**k)]=F[j]*(prod)
                    k+=1
                    prod+=i**k
for i in range(2,M+1):
    F[i]+=F[i-1]

for i in L:
    print(F[i])