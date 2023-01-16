def pmp(a,b):
    rst=1
    pdt=a
    for i in range(b):
        rst*=a
        a-=1
    return rst

T=int(input())


for i in range(T):
    text=input().split(' ')
    a=int(text[0])
    b=int(text[1])
    print(int(pmp(b,a)/pmp(a,a)))
    
