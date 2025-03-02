

a,b = map(int,input().split())

def gcd(a,b):
    while a:
        a,b = b%a, a
    return b


g = gcd(a,b)
a = a//g
b = b//g

for i in range(1,int(g**0.5)+1):
    if g%i:
        continue
    h = g//i
    print(i, h*a, h*b)
    if h!=i:
        print(h, i*a, i*b)
