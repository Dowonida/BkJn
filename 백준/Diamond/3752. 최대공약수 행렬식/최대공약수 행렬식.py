'''
오일러 p함수를 빠르게 구할 수 있나?

1. 최초소인수 모두 구하기
2. 오일러피 함수 메모라이징


소인수는 최대 10개


루트까지의 소수만 전부 구해둠
1) 10만보다 큰 경우 - prime을 순회하면서 최대한 나누기
2) 10만보다 작은 경우 pp[i]로 나누기

'''


import sys
input = sys.stdin.readline
MOD = 1000000007

#MAX = 200
MAX = 100000
pp = [0]*MAX
prime = []

for i in range(2,MAX):
    if pp[i] == 0:
        prime.append(i)
        pp[i] = i
    for p in prime:
        cnt = i*p
        if cnt>=MAX:
            break

        pp[cnt] = p

        if i%p == 0:
            break


def func(n):
    answer = n
    cnt = n
    for p in prime:
        if cnt<100000:
            break
        if cnt%p ==0:
            answer = answer*(p-1)//p
            while cnt%p == 0:
                cnt//=p
    else: # cnt>100000 -> 10만 이상의 소수
        answer = answer*(cnt-1)//cnt
        return answer
    while cnt>1:
        div = pp[cnt]
        answer = answer*(div-1)//div
        while cnt%div == 0:
            cnt//=div
    return answer
        

            


for _ in range(int(input())):
    input()
    rst = 1
    for i in map(int,input().split()):
        rst = (rst*func(i))%MOD
    print(rst)
