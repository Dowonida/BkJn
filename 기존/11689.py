n=int(input())
cnt={}
for i in range(2,int(n**(0.5))+1):
    if n%i==0:
        while n%i==0:            
            n=n//i
        cnt[i]=1
print(i,cnt)