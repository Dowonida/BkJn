def GCD(a,b):
    while a:
        a,b=b%a,a
    return b

n,k= map(int,input().split())

gcd=1

for i in range(2,n+1):
    a=GCD(k,i)
    if a!=1:
        gcd=gcd*a
        if k%a!=0:
            print(k,a)
            break
        k=k//a

print(gcd)
