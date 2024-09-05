import sys
input = sys.stdin.readline
# 모든 숫자는 30자리 이진법으로 바꾼다.
def num(n):
    a = []
    for i in range(30):
        a.append((n%2))
        n//=2
    return a[::-1]

# '' = 1
# '0' = 2
# '1' = 3
# '00' = 4

dic = {} #안에 몇 개의 숫자가 있는지
for i in range(31):
    dic[1<<i] = 1

for _ in range(int(input())):
    a,b = map(int,input().split())
    s = num(b)

    idx = 1

    if a == 3:
        rst = 0
        for i in range(30):
            T = idx*2+1
            F = idx*2
            if s[i]:
                T,F = F,T
            
            if T in dic and dic[T]: #정배
                idx = T
                rst += 1<<(29-i)
            else:
                idx = F

        print(rst)
    elif a == 2:
        for i in range(30):
            idx = idx*2 + s[i]
            dic[idx] -= 1
    else:
        for i in range(30):
            idx = idx*2 + s[i]
            if idx not in dic:
                dic[idx] = 0
            dic[idx] += 1
        
