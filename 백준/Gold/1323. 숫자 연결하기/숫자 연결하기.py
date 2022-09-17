n, m = input().split()
p=10**len(n)
n=int(n)
m=int(m)

gg,gcd=m,p
while gg:
    gg, gcd= gcd%gg, gg

mg=m//gcd#최대 반복 횟수
rest=p%m

if n%(gcd)!=0:
    print(-1)
else:
    rst=0
    plus=n%m
    for i in range(1,mg+1):
        rst+=plus
        plus=(plus*p)%m
        if rst%m==0:
            print(i)
            break
    else:
        print(-1)
