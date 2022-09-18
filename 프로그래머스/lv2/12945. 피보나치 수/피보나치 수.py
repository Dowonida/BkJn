fib=[0]*100001
fib[1]=1
for i in range(2,100001):
    fib[i]=fib[i-1]+fib[i-2]
def solution(n):
    answer = fib[n]%1234567
    return answer