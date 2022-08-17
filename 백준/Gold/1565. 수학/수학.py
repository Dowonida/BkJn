def gcd(a,b):
    while a:
        a,b=b%a,a
    return b

def lcm(a,b):
    return a*b//gcd(a,b)

x,y=map(int,input().split())
D=list(map(int,input().split()))
M=list(map(int,input().split()))
a=D[0]
b=M[0]
for i in range(1,x):
    a=lcm(a,D[i])
for j in range(1,y):
    b=gcd(b,M[j])
if b%a!=0:
    print(0)
else:
    cnt=0
    bfactor=set()
    for i in range(1,int(b**(0.5))+1):
        if b%i==0:
            bfactor.add(i)
            bfactor.add(b//i)
    for i in bfactor:
        cnt+= (not i%a)
    print(cnt)
