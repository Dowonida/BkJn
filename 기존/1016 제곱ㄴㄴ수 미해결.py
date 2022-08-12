m, M=map(int,input().split())
#Mx=100
Mx=1000000
DP=[1]*(Mx+1)
#인덱스가 0부터 마지막숫자까지
#100만까지의 소수의 제곱수
Prime=[]
for i in range(2,Mx):
    if DP[i]==1:
        Prime.append(i**2)
        k=1
        while i*k<=Mx:
            DP[i*k]=0
            k+=1
#print(Prime)
DP=[1]*(M-m+1)
for i in Prime:
    mok=(m//i)*i-m
    if mok<0:
        mok+=i
    while mok<=M-m:
        DP[mok]=0
        mok+=i
print(sum(DP))