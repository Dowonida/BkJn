import sys
#메모리가 충분해보이므로 테스트케이스에서 가장 큰값을 기준으로
#전부 구한 다음 불러오기
T=int(sys.stdin.readline())
L=[]
for i in range(T):
    L.append(int(sys.stdin.readline()))
M=max(L) #테스트 케이스가 오름차순이라는 보장이 없기때문

#에라스토테네스의 체와 소수합 작성을 동시에 가능할듯
#기존 사전에 없으면 소수목록에 추가
#기존 소수합 목록에서 해당 수를 거듭곱하기
F={1:1}
for i in range(2,M+1):
    if i not in F:#새로운 소수가 추가될때마다 모든 합성수의 값을 채울거임
        #F[i]=i+1
        Basic=list(F.keys())# 기존의 숫자들
        for j in Basic:
            k=1#지수
            prod=1+i #현재 계수
            #계수란 기존수에 곱해진 값을 말한다.
            #예를 들어 i가 2인경우 key값에 2,4,8...을 곱하게되면
            #value에는 1+2, 1+2+4....가 곱해지게 되는데 이 1+2를 계수라고 하자.
            #현재 계수는 이전 계수+i^현재지수가 된다.
            while j*(i**k)<=M:
                F[j*(i**k)]=F[j]*(prod)
                k+=1
                prod+=i**k
for i in range(2,M+1):
    F[i]+=F[i-1]

for i in L:
    print(F[i])