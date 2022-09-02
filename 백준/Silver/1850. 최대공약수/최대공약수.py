a,b=map(int,input().split())
while a:
    a,b=b%a,a
print('1'*b)
