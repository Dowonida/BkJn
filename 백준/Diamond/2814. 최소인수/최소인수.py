N,P = map(int,input().split())

prime = []
#N=32000

L = [0]*(P)

#P=31627
#P=7
for i in range(2,P):
    if L[i] == 0:
        prime.append(i)
        L[i] = i
    for j in prime:
        if i*j>=P:
            break
        L[i*j] = j
        if i%j == 0:
            break

LL = len(prime)
'''
P는 32000까지만 하면 된다.
32000을 넘는 P라면 두번째가 이미 1e9를 넘어감

그럼 소수는 3403개이고
K를 P로 나눈 다음, P이하의 소수들의 합성만 고려하면되니까
금방 할 듯
'''
def func(K,P):
    #마지막 인덱스가 prime보다 길면 빠져나간다.
    #마지막까지의 곱이 K보다 크면 빠져나간다.
    #빠져나갈때는 rst를 계산하고, 직전 인덱스에 1을 더함
    
    #스택에 추가될 때 값을 곱해준다면?
    #
    K//=P #P의 배수만 세면 되기 때문
    rst = K
    stk = [0]
    base = 1
    sgn = 1
    while stk:
        idx = stk[-1]
        if idx == LL:
            stk.pop()
            if stk:
                base//=prime[stk[-1]]
                sgn *= -1
                stk[-1]+=1
            continue
        cur_p = prime[idx]
        base *= cur_p
        sgn *= -1
        
        if base > K:
            base//=cur_p
            stk.pop()
            if stk:
                base//=prime[stk[-1]]
                stk[-1]+=1
            continue
        rst += sgn*(K//base)
        stk.append(idx+1)
    return rst
        
          
if P>31607 and N>1:
    print(0)
else:
    rst = 0
    cnt = 1<<29
    while cnt:
        if N>func(rst+cnt-1,P):
            rst += cnt
        cnt//=2
    if rst<=1000000000:
        print(rst)
    else:
        print(0)
        
'''
PK인데 K는 1~P-1의 소수로 나눠지면 안됨
다시말해 1~K까지 1~P-1의 배수 개수를 빼면 됨
K- K//2 - K//3 - K//5 ... +K//6+K//10....를 구하면
PK 이하의 최소인수가 P인 수의 개수가 나옴
물론 꼭 P의 배수일 필욘 없음 PK 대신 임의의 N



'''
