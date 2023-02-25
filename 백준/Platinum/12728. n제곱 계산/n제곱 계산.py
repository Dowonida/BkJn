import sys
input = sys.stdin.readline

dic={}
dic[0]=(1,0) #항등원
dic[1]=(3,1) #2의 0제곱인 경우 자연수가 1, 루트5가 0개
def func(a,b):

    return ( (a[0]*b[0]+5*a[1]*b[1])%1000,
             (a[1]*b[0]+a[0]*b[1])%1000)
    
#2의 30제곱까지만
for i in range(1,31):
    dic[1<<i]=func(dic[1<<(i-1)],dic[1<<(i-1)])


for _ in range(1,1+int(input())):
    cnt = 0
    rst = (1,0)
    n = int(input())
    for i in range(31):
        if n&(1<<i):
            cnt+=1<<i
            if cnt in dic:
                rst = dic[cnt]
            else:
                rst = func(rst,dic[1<<i])
                dic[cnt]=rst

    print( f'Case #{_}:',format((2*rst[0]-1)%1000,'03'))
