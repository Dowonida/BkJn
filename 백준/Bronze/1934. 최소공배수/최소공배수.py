T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    A,B=a,b
    while A:
        (A,B)=(B%A,A)
    print(a*b//B)