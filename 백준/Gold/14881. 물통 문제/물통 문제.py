import sys
input=sys.stdin.readline
def gcd(a,b):
    while a:
        a,b=b%a,a
    return b

T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    if c%gcd(a,b)==0 and c<=max(a,b):
        print("YES")
    else:
        print("NO")