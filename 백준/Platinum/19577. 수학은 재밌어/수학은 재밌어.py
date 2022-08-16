import sys
input=sys.stdin.readline

def func(n):
    m=n
    for i in range(2,int(n**(0.5)+1)):
        if m%i==0:
            while m%i==0:
                m//=i
            n=(n//i)*(i-1)
    if m>1:
        n=(n//m)*(m-1)
    return n


N=int(input())
factor=[]
for i in range(1,int(N**(0.5)+1)):
    if N%i==0:
        factor.append(N//i)
for i in factor:
    if i*func(i)==N:
        print(i)
        break
else:
    print(-1)
