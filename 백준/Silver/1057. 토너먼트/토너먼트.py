a, b, c = map(int,input().split())

cnt=0
while b!=c:
    cnt+=1
    b=(b+1)//2
    c=(c+1)//2
print(cnt)